from flask import Flask, request, render_template, redirect
from requests import get
import mysql.connector
from flask_cors import CORS
from dotenv import load_dotenv
from os import environ
from urllib.parse import urlparse

#load env variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# connect to database
timeout = 10
conn = mysql.connector.connect(

    host=environ.get("DB_HOST"),

    user=environ.get("USER"),

    password=environ.get("PASSWORD"),

    database="urls",

    port=environ.get("DB_PORT"),

    connect_timeout = timeout
)

# convert url id to base62 (Bing AI chat was helpful for this) 
def shorten_key(num):
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = []
    while num > 0:
        num, rem = divmod(num, len(BASE62))
        key.append(BASE62[rem])
    key.reverse()
    return ''.join(key)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():
    db = conn.cursor()
    try:
        url = request.form.get("url")
        if urlparse(url).netloc == urlparse(request.url_root).netloc:
            return render_template("erorr.html", erorr="Can't do that ;)")
        
        # check if url is valid
        if get(url).status_code == 200:
            # check if url is already in database
            db.execute("SELECT * FROM urls WHERE long_url = %s",[url])
            short_url = db.fetchall()
            if short_url:
                # if url is already in database return the short url
                return render_template("shorturl.html", short_url=short_url[0][2])
            
            # else get the next id to convert to base62
            db.execute("SELECT MAX(id) FROM urls")
            key = shorten_key(db.fetchall()[0][0] + 1)
            
            # insert url into database with the converted id as a key
            to_insert = [str(url), (request.url_root + key)]
            db.execute("INSERT INTO urls (long_url, short_url) VALUES (%s, %s)", to_insert)
            conn.commit()
            # return the short url to the user
            return render_template("shorturl.html", short_url=to_insert[1])
        conn.close()
        # if url is invalid return an error
    except Exception:
        return render_template("erorr.html", erorr="Incorrect URL")
        
@app.route("/<short_url>")
def shorturl(short_url):
    db = conn.cursor()
    # check if short url is in database
    db.execute("SELECT * FROM urls WHERE short_url = %s", [(request.url_root + short_url)])
    found = db.fetchall()
    # if short url is in database redirect to the long url
    if found:
        return redirect(found[0][1])
    # else return an error
    else:
        return render_template("erorr.html", erorr="URL not found")

