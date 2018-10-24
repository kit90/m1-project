"""Module containing the Movie class."""

import webbrowser

class Movie():
    """The class representing a movie.

    Attributes:
        title (str): The title of the movie.
        storyline (str): A short summary of the movie's plot.
        poster_image_url (str): The URL of a poster image.
        trailer_youtube_url (str): The URL of a trailer available on YouTube.

    """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Constructor for the Movie object.

        Args:
            movie_title (str): The title of the movie.
            movie_storyline (str): A short summary of the movie's plot.
            poster_image (str): The URL of a poster image.
            trailer_youtube (str): The URL of a trailer available on YouTube.

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the trailer in a web browser."""
        webbrowser.open(self.trailer_youtube_url)
