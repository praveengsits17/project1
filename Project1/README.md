In this project I made a book review website where a user can login and search for a book by its any of the attributes such as title, author name or ISBN number. User can also see reviews from other users and can write his personal review about the book too. User can also see ratings from book review site 'Goodreads'. An API is also included which returns the JSON object containing details about the book and its ratings.




1. books.csv
 
This is the main CSV file from where I imported the books data to my Heroku Database.

2. import.py

Python file written to insert data from csv file into the Heroku Database.

3. helpers.py

In this Python file I have defined the 'login_required()' function.

4. application.py
 
This is the main application file written in Python which have the routes to various pages of the website.

5. static folder

This foldder conatins an image file goodreads.jpg and some CSS files named style.css, login.css, results.css.

6. templates folder

This folder contains 7 HTML files.
  
  1. layout.html
     This is the basic html layout file. It is inherited by other html files to show similar layout on every page.
    
  2. login.html
     This file contains the html for the login page.
  
  3. register.html
     This file contains the html for new registration.
     
  4. index.html
     This file is loaded when an user successfully logs in.
    
  5. results.html
    This file contains the html for displaying the results of search according to the details entered.
  
  6. book.html
     This file contains the html for displaying the details of a particular book when it is being searched by the user.
    
  7. error.html
     File for displaying errors like wrong user trying to logg in.

I have used three tables.

1. books(id, isbn, title, author, year)
2. users(id, username, hash)
3. reviews(id, user_id, book_id, comment, rating, time)

I have joined the tables according to the requirement.

# ENV Variables
$ export FLASK_APP = application.py # flask run
$ export DATABASE_URL ="postgres://vkjdurkswbkezm:6f88588230ce58dd5b065f0cdd2eb3659b43bc58692acd0311881d76ce158b1a@ec2-52-72-65-76.compute-1.amazonaws.com:5432/dd54sjh78r1874"
$ export GOODREADS_KEY ="D9AwPRJqge9JqfmiTkmlcw" 
