"""Creates and displays a web page containing movie information."""

import media, fresh_tomatoes

# Define each movie's attributes.
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a"
                     " unique mission becomes torn between following his"
                     " orders and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

mad_max_fury_road = media.Movie("Mad Max: Fury Road",
                                "A woman rebels against a tyrannical ruler in"
                                " postapocalyptic Australia in search for her"
                                " home-land with the help of a group of female"
                                " prisoners, a psychotic worshipper, and a"
                                " drifter named Max.",
                                "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=hEJnMQG9ev8")

aliens = media.Movie("Aliens",
                     "The moon from Alien (1979) has been colonized, but"
                     " contact is lost. This time, the rescue team has"
                     " impressive firepower, but will it be enough?",
                     "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=AW-7_HE98PY")

_2001_a_space_odyssey = media.Movie("2001: A Space Odyssey",
                                    "Humanity finds a mysterious, obviously"
                                    " artificial object buried beneath the"
                                    " Lunar surface and, with the intelligent"
                                    " computer H.A.L. 9000, sets off on a"
                                    " quest.",
                                    "https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg",  # NOQA
                                    "https://www.youtube.com/watch?v=XHjIqQBsPjk")  # NOQA

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc"
                              " and chaos on the people of Gotham, the caped"
                              " crusader must come to terms with one of the"
                              " greatest psychological tests of his ability to"
                              " fight injustice.",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

zootopia =  media.Movie("Zootopia",
                        "In a city of anthropomorphic animals, a rookie bunny"
                        " cop and a cynical con artist fox must work together"
                        " to uncover a conspiracy.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=bY73vFGhSVk")

# List of all movies in the web page.						
movies = [avatar, mad_max_fury_road, aliens, _2001_a_space_odyssey,
          the_dark_knight, zootopia]

# Create the web page and open it in a web browser.
fresh_tomatoes.open_movies_page(movies)
