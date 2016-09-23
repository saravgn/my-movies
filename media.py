import webbrowser


class Movie ():

    '''this class describes a movie. A movie has some features such as
    a title, a storyline, a poster image, a tailer and actors'''

    def __init__(self, movie_title, storyline, poster_image,
                 trailer_youtube, movie_actors, imdb_url):

        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = movie_actors
        self.imdb = imdb_url

    def showTrailer(movie):

        '''this function shows the movie trailer'''

        webbrowser.open(movie.trailer_youtube_url)

    def printInfo(self):

        '''other utilities'''

        print (self.__doc__)
        print (self.__module__)
