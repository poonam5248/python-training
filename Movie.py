'''Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
Make methods to
1. Display-Display the details.
2. Update- Update the movie details.'''





class MovieDetails:
    def __init__(self, moviename, artistname, year_of_release, ratings):
        self.moviename = moviename
        self.artistname = artistname
        self.year_of_release = year_of_release
        self.ratings = ratings

    print("")

    def display(self):
        print("Movie: ", self.moviename)
        print("artist name: ", self.artistname)
        print("release year:", self.year_of_release)
        print("ratings out of 5: ", self.ratings)


    print("")
    def update(self):
        self.moviename = input("enter the new updated movie:")
        self.artistname = input("enter the artist name:")
        self.year_of_release = (input("enter its release year:"))
        self.ratings = (input("enter the rating out of 5:"))

    print("")
moviename = input(" Movie: ")
artistname = input("Artist name")
year_of_release = input("Release year:")
ratings = input("Rating out of 5:")
s1 = MovieDetails(moviename, artistname, year_of_release, ratings)
s1.display()
s1.update()
s1.display()
