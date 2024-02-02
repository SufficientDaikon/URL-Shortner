<p>Ever found something really cool on the interwebs that you wanted to share with your friends, but when you went to copy the URL for said cool thing you found that it's just a bit too long and a lil ugly?, it's a problem
we all face, which is why i made this one of a kind project that no one has thought of before, to help you make those long, ugly URLs shareable, this... is my gift to the world.</p>
<h1 align="center">
 URL50
</h1>
<h4 align="center">a custom URL shortener with Flask and MySQL</h4>
<p align="center">
 Built with ❤︎ 
</p>
</br>

## Explanation
- This app takes the URL you input, it stores it in the Database, then it generates a BASE62 key assosiacted with it, and generates a shorter URL using the key.
- the database is a mysql DB hosted on [Aiven](https://aiven.io/).
- [Bootstrap](https://getbootstrap.com/) has been used for many of the UI elements across the app, barring a few exceptions 
- the font for the "logo" comes from [Google fonts](https://fonts.google.com/)
- the app is deployed on [render](https://render.com/)
  
## Diagram
![image](https://github.com/SufficientDaikon/URL-shortner/assets/65625347/5a4d9295-ee4c-4261-9697-779841353046)


## Demo
![dssds](https://github.com/SufficientDaikon/URL-shortner/assets/65625347/af8b814f-8f66-4827-96bb-dc55d49b1c50)

<h4 align="center"> <a href="https://url-50.onrender.com/">Try it out your self</a> </h4>

## Files
- ### app.py
  holds the main body of the webapp's Code, as well as the code to connect to the DB, and has four functions
  - #### index()
	simply loads the main homepage of the app and is the default route of the app.
  - #### shorten_key()
	which takes a number and converts it to a BASE62 string, the idea is to take the id for the url in the database, and convert it to BASE62, and the result will be the key for the shortened url, chose to do it this way because 	if i used a random number generator there will always the chance of duplicates so this method would prevent that from ever being the case, i did use the help of an AI assistant to help with the python code.
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

  ## Extras
  - For security reasons i had to find a way to abstract the DB information from the application code, there were many ways, the one i settled with is using environment variables to store the actaul information abstracted away as  generic variables, in a .env file, then i loaded it into the app and instead of hardcoding the DB info, i used these variables instead.
   - when deciding what DBMS to go with, it was either SQLite or learn something new, i went with the latter and chose MySQL simply because i wanted to learn MySQL as i was doing this project.
   - Bing Copilot was used as direct help twice, some UI elements in the front end, and helped with the shorten_key() function.
   - i decided to go with the flask framework for this project because i felt i wasn't comfortable enough with it to move on to something else yet.
     
   
