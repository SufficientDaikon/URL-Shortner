<h1 align="center">
 URL50
</h1>

<h4 align="center">Creating custom URL shortener with Flask</h4>
<p align="center">
 Built with ❤︎ 
</p>
</br>
## Architecture

## Explanation 

- ### app.py
  holds the main body of the webapp's Code, it's functions, and all that relates to what happens behind the scenes.
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
