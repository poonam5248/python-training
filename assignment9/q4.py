#q4  Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.

class MovieDetails:
	def __init__(self,movname,artname,year,rating):
		self.movname=movname
		self.artname=artname
		self.year=year
		self.rating=rating
	print("")
		
	def display(self):
		print("movie",self.movname)
		print("artist name",self.artname)
		print("release year:",self.year)
		print("rating out of 5",self.rating)
	print("")
	def update(self):
		self.movname=input("enter the new updated movie")
		self.artname=input("enter the artist name")
		self.year=(input("enter its release year"))
		self.rating=(input("enter the rating out of 5"))
		
movname=input(" movie")
artname=input("artist name")
year=(input("release year"))
rating=(input("rating out of 5"))		
s1=MovieDetails(movname,artname,year,rating)
s1.display()
s1.update()
s1.display()