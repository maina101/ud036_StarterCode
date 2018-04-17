import webbrowser

# create Movie class


class Movie():
    # Movie class helps create multiple instances of the class using the class as a
    # template or blue print for all the movies in the website. The class will supply
    # data attributes like the title, the story line, URL to the poster picture and 
    # URL to the movie trailers
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
