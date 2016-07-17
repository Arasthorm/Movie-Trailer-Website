''' Individual data for each movie. '''

import fresh_tomatoes
import media

# varialbes for each movie in my media library


INTERSTELLAR = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "https://lh5.googleusercontent.com/-_LZCNOpWcfI/AAAAAAAAAAI/AAAAAAAAAq4/9oovHx0Oouo/s0-c-k-no-ns/photo.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")


PULP = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    "http://johnalberti.net/wp-content/uploads/2016/06/Pulp-Fiction-Poster.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

LORD = media.Movie(
    "The Lord of the Rings: The Return of the King",
    "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
    "http://vignette4.wikia.nocookie.net/lotr/images/7/77/The_Return_of_the_King_Poster_01.jpg/revision/latest?cb=20150203042330",
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

MATRIX = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")



# pass each instance of movie to a list and generate an html with
# open_movies_page method
MY_MOVIES = [INTERSTELLAR, PULP, LORD, MATRIX]
fresh_tomatoes.open_movies_page(MY_MOVIES,"Arasthorm")

