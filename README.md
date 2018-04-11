# ud036_StarterCode
Starter Code
TITLE : Movie Trailer Website 
AUTHOR : Charles Gatoto
PYTHON VERSION : Python 2.7.9
PROJECT : A python file generating a html web page
CODE CHECKER USED: PEP8
Description: This code stores a list of 6 of my favorite movies, gets the movie posters from wikipedia, a movie trailer URL, and  together opens this data as web page; visitors to the webpage will click on the movie poster to access link to the movie trailer.

This readme file gives a detailed explanation of how the website is created using; fresh_tomatoes.py functions with media.py and playMovieTrailer.py to display movie title, poster_image, and the movie trailer. 
I have uploaded this file to my github account that i will give access if anyone wants to review my files and run my website. 

WEBSITE PLAN
Using Python program IDLE 

STEPS
	- To go to the website, i have a file ***** that is used to dynamically generate the webpage which automates the process instead of manual double click to open the HTML file. 
	- All the 6 movie posters will be displayed on the main page/landing page. 
	- Click on any poster of the movie you want to play it's trailer

CODING
We have several movies that will be on the website, so a CLASS called Movies is created as a blue print whose attributes will be inherited by all the movies. The Class is saved in a python file called media.py
With the generic blue print of movies created (class), instances will be created which will inherit the characteristics of the CLASS. 

The properties that will be passed to the movies from the Class will be:
	- Movie title
	- Movie storyline
	- Poster image of the movie
	- trailer URL 
Once the __init__ function is called all the variables associated with the movies will be initialized. 
example: Car2.storyline will print out the correct movie story line. 

A method is created to open the webbrowser which has to be imported in the media file. Show_trailer () which takes one argument (self)

Defining the class
Created a file called media.py. Inside of it, start our Movie class by typing:

class Movie():
created another file playMovieTrailer.py and this is used to call the class Movie properties that will be used in the media.py file
import media

cars_2 = media.Movie()
This calls the function called init to create a new instance of the class by assigning space in the computer's memory for the instance.

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
         self.title = movie_title
         self.storyline = movie_storyline
         self.poster_image_url = poster_image
         self.trailer_youtube_url = trailer_youtube
		

import media #here is an example of what goes into the constractor
fresh_tomatoes.py has to be imported as well as this is the file the creates the HTML file that plays the movie website.

cars_2 = media.Movie(" A Car story",
                     "A hollywood wanna be",
					 "The car2 movie is a continuation of the cars1. Mcqueen has gone to the international stage and now is being recognized and he is about to make his brand once he wins the repeat race since the other race did not have a definate winner." #  NOQA
                     "https://vignette.wikia.nocookie.net/pixar/images/f/f5/Cars-2-movie-poster-cast-hi-res-01.png/revision/latest?cb=20110525161429",  # NOQA
                     "https://www.youtube.com/watch?v=VophA5oity4")

Movie Website
fresh_tomatoes.py is used in the playMovieTrailer code to open the movie page so we have to import it into the file. Then from here the list is created of all the movies that will play on the website. 

movies = [cars_2, Boss_Baby, Turbo, Rio, Ratatouille, Minions]
fresh_tomatoes.open_movies_page(movies)

HOW TO RUN THE PROGRAM!!!
- Ensure that you have Python 2.7.9 or later version installed into the terminal (computer).
- Download fresh_tomatoes.py file which is also in my account in GITHUB. Make sure these files(media.py, playMovieTrailer.py, and fresh_tomatoes.py) are present in the same folder.
- Open these files using IDLE.
- The playMovieTrailer.py file will be opened and it will be responsible for generating the HTML page or Website [fresh_tomatoes.html], using the fresh_tomatoes.py file.
