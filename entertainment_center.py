import media
import fresh_tomatoes
import operator


# movies instances
fantastic_four_actors = "Michael B Jordan, Kate Mara, JamieBell, Miles Teller"
fantastic_four = media.Movie(
          "Fantastic4",
          "four fantastic friends work together to protect the world",
          "https://upload.wikimedia.org/wikipedia/en/f/f4/Fantastic_Four_2015_poster.jpg",  # noqa
          "https://www.youtube.com/watch?v=DMEa0CJbAUs",
          fantastic_four_actors,
          "http://www.imdb.com/title/tt1502712/")

ghost_rider_actors = "Nicolas Cage, Matt Long, Eva Mendes"
ghost_rider = media.Movie(
          "Ghost rider",
          "Stunt motorcyclist Johnny Blaze gives up his soul to become"
          "a hellblazing vigilante, to fight against power hungry"
          "Blackheart, the son of the devil himself.",
          "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghost_Rider_2_Poster.jpg",  # noqa
          "https://www.youtube.com/watch?v=L-WTmTOi0zU",
          ghost_rider_actors,
          "http://www.imdb.com/title/tt0259324/")

beastly_actors = "Alex Pettyfer, Vanessa Hudgens, Mary-Kate Olsen"
beastly = media.Movie(
          "Beastly",
          "Beastly is a retelling of the fairytale Beauty and"
          "the Beast and is set in modern-day New York City.",
          "https://upload.wikimedia.org/wikipedia/en/0/03/Beastly_new_n.jpg",  # noqa
          "https://www.youtube.com/watch?v=Neo6W1f7hyY",
          beastly_actors,
          "http://www.imdb.com/title/tt1152398/")

butterfly_effect_actors = "Ashton Kutcher, John Patrick Amedori, Logan Lerman"
butterfly_effect = media.Movie(
          "The butterfly effect",
          "The title refers to the butterfly effect,a popular hypothetical"
          "example of chaos theory which illustrates how small initial"
          "differences may lead to large unforeseen consequences over time.",
          "https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg",  # noqa
          "https://www.youtube.com/watch?v=NeV0MvU1Uhs",
          butterfly_effect_actors,
          "http://www.imdb.com/title/tt0289879/")


cinderela_story_actors = "Hilary Duff, Hannah Robinson, Chad Michael"
cinderela_story = media.Movie(
          "A cinderela story",
          "A teen comedy musical dance film about Cinderella story",
          "https://upload.wikimedia.org/wikipedia/en/b/b3/Movie_poster_a_cinderella_story.jpg",  # noqa
          "https://www.youtube.com/watch?v=B_VFs9j95gc",
          cinderela_story_actors,
          "http://www.imdb.com/title/tt0356470/")

about_a_boy_actors = "Hugh Grant, Nicholas Hoult, Toni Collette"
about_a_boy = media.Movie("About a boy",
          "About a boy is an adaptation of the 1998 novel of the same name"
          "by Nick Hornby. It is about the relation-ship between father"
          "ad son.",
          "https://upload.wikimedia.org/wikipedia/en/3/3d/About_a_boy_movie_poster.jpg",  # noqa
          "https://www.youtube.com/watch?v=-apwoGTpi7E",
          about_a_boy_actors,
          "http://www.imdb.com/title/tt0276751/")

kill_bill_actors = "Uma Thurman, David Carradine, Shun Sugata"
kill_bill = media.Movie("Kill bill",
          "Kill Bill is an American two-part martial arts film, as well as"
          "the fourth film written and directed by Quentin Tarantino."
          "It talks about the story of a girl asking for revenge.",
          "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",  # noqa
          "https://www.youtube.com/watch?v=7kSuas6mRpk",
          kill_bill_actors,
          "http://www.imdb.com/title/tt0266697/")

# movies is a list of the movie instances
movies = [
        fantastic_four,
        ghost_rider,
        beastly,
        butterfly_effect,
        cinderela_story,
        about_a_boy,
    ]

# open my movies website
fresh_tomatoes.open_movies_page(movies)
