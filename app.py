from flask import Flask, request, render_template, redirect
from requests import get
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(

    host="loclalhost",

    user="admin",

    password="1234",

    database="url"

)

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
        if get(url).status_code == 200:
            db.execute("SELECT * FROM urls WHERE long_url = %s",[url])
            short_url = db.fetchall()
            if short_url:
                return render_template("shorturl.html", short_url=short_url[0][2])

            db.execute("SELECT MAX(id) FROM urls")
            key = shorten_key(db.fetchall()[0][0] + 1)
            
            to_insert = [str(url), ("127.0.0.1:5000/"+ key)]
            db.execute("INSERT INTO urls (long_url, short_url) VALUES (%s, %s)", to_insert)
            conn.commit()
            return render_template("shorturl.html", short_url=to_insert[1])
        conn.close()
    except Exception:
        return render_template("erorr.html", erorr="Incorrect URL")
        
@app.route("/<short_url>")
def shorturl(short_url):
    db = conn.cursor()

    db.execute("SELECT * FROM urls WHERE short_url = %s", ["127.0.0.1:5000/"+ short_url])
    found = db.fetchall()
    if found:
        return redirect(found[0][1])
    else:
        return render_template("erorr.html", erorr="URL not found")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)