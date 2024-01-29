<h1 align="center">
 URL50
</h1>

<h4 align="center">Creating custom URL shortener with Flask and MySQL</h4>
<p align="center">
 Built with ❤︎ 
</p>
</br>

## Architecture

## Explanation 
- ### app.py
  holds the main body of the webapp's Code, as well as the code to connect to the DB, and has four functions
  - #### index()
    simply loads the main homepage of the app and is the defult route of the app.
  - #### shorten_key()
    which takes a number and converts it to a BASE62 string, the idea is to take the id for the url in the database, and convert it to BASE62, and the result will be the key for the shortend url, that way there will never be duplicates because the id will always be different.
  - #### shorten()
    this function gets called when there is a url that is sent to the server, it first checks if the url is vaild and accessible, if it is, it then checks the DB for a duplicate, if there isn't, it then inserts it into the DB and calles the shorten_key() function with the passing in the id of the newly inserted url, and inserts the result of that function into the DB as the shortened url
    
    
- ### run.py
  holds the argument that loads the app for gunicorn
- ### requirements.txt
  a list of all the libraries and modules that need to be installed in the env to get the app to work.
- ### static
  - #### style.css
    holds the custom CSS used throughout the app
- ### templates
  - #### layout.html
    holds the code for the defult html from which the all the app's pages are derived
  - #### index.html
    holds the html for the main homepage
  - #### erorr.html
    holds the html for the erorr page
  - #### shorturl.html
    holds the html for displaying the shortend URL
