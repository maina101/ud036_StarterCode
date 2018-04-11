import media
import fresh_tomatoes

cars_2 = media.Movie(" A Car story",
                     "hollywood wanna be",
                     "https://vignette.wikia.nocookie.net/pixar/images/f/f5/Cars-2-movie-poster-cast-hi-res-01.png/revision/latest?cb=20110525161429",  # NOQA
                     "https://www.youtube.com/watch?v=VophA5oity4")

Boss_Baby = media.Movie("Bossy Baby",
                        "A baby who got everything he wanted by being bad",
                        "https://vignette.wikia.nocookie.net/transcripts/images/3/3a/DreamWorks%27_The_Boss_Baby_-_iTunes_Movie_Poster.jpg/revision/latest?cb=20170417155106",  # NOQA
                        "https://www.youtube.com/watch?v=tquIfapGVqs")

Turbo = media.Movie("Turbo",
                    "Snail that won a race against very fast cars who did not pay attention",  # NOQA
                    "https://vignette.wikia.nocookie.net/turbo-dreamworks/images/d/d3/Turbo_Movie_Poster.jpg/revision/latest?cb=20130721184651",  # NOQA
                    "https://www.youtube.com/watch?v=_sjzBa3kVQM")

Rio = media.Movie("Rio -All about the BIRD",
                  "story of a bird that was kidnapped and taken to south America",  # NOQA
                  "https://vignette.wikia.nocookie.net/rio/images/7/7e/Rio-movie-poster.jpg/revision/latest?cb=20130725132605",  # NOQA
                  "https://www.youtube.com/watch?v=BG-fC-O_uQE")

Ratatouille = media.Movie("Ratatouille",
                         "Story of a rat that helped a restaurant owner to get fame our of a rat receipe",  # NOQA
                         "https://projectedrealities.files.wordpress.com/2014/01/ratatouillec.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=JapaA3ZwA_4")

Minions = media.Movie("Minions",
                      "I have no clue about what this movie is but children love it",  # NOQA
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcRbHFoQWQZLymKtwzfjVEvfNDOIdcWOL-tUFstMC00m5OMf961D",  # NOQA
                      "https://www.youtube.com/watch?v=P9-FCC6I7u0")

movies = [cars_2, Boss_Baby, Turbo, Rio, Ratatouille, Minions]
fresh_tomatoes.open_movies_page(movies)
