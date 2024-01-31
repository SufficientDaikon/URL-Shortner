<h1 align="center">
 URL50
</h1>

<h4 align="center">Creating custom URL shortener with Flask and MySQL</h4>
<p align="center">
 Built with ❤︎ 
</p>
</br>

## Diagram
![image](https://github.com/SufficientDaikon/URL-shortner/assets/65625347/5a4d9295-ee4c-4261-9697-779841353046)


## Demo
![vado](https://github.com/SufficientDaikon/URL-shortner/assets/65625347/97dda7bd-2334-4fbd-b649-4dbcbedf608a)

## Explanation
- ### app.py
  holds the main body of the webapp's Code, as well as the code to connect to the DB, and has four functions
  - #### index()
	simply loads the main homepage of the app and is the default route of the app.
  - #### shorten_key()
	which takes a number and converts it to a BASE62 string, the idea is to take the id for the url in the database, and convert it to BASE62, and the result will be the key for the shortened url, that way there will never be duplicates because the id will always be different.
  - #### shorten()
	this function gets called when there is a url that is sent to the server, it first checks if the url is valid and accessible, if it is, it then checks the DB for a duplicate, if there isn't, it then inserts it into the DB and calls the shorten_key() function with the passing in the id of the newly inserted url, and inserts the result of that function into the DB as the shortened url
  - #### shorturl()
	this function is responsible for redirecting users IE, it checks the DB for the URL that is linked to the short URL and redirects the browser to the orignal URL
- ### run.py
  holds the argument that loads the app for gunicorn
- ### requirements.txt
  a list of all the libraries and modules that need to be installed in the env to get the app to work.
- ### static
  - #### style.css
	holds the custom CSS used throughout the app
- ### templates
  - #### layout.html
	holds the code for the default html from which the all the app's pages are derived
  - #### index.html
	holds the html for the main homepage
  - #### erorr.html
	holds the html for the error page
  - #### shorturl.html
	holds the html for displaying the shortened URL

