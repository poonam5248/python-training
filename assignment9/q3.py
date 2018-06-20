#q3  Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
	
class temperature:
	def __init__(self,celsius,fahrenheit):
		self.celsius=celsius
		self.fahrenheit=fahrenheit
		
	def convertfahrenheit(self):
		fahrenheit=(celsius * 1.8) + 32
		print(fahrenheit)
		
	def convertcelcius(self):
		celsius=(fahrenheit - 32) / 1.8
		print(celsius)
		
celsius=int(input("enter temp in celcius"))
fahrenheit=int(input("enter temp in fahrenheit"))

s1=temperature(celsius,fahrenheit)
s1.convertfahrenheit()
s1.convertcelcius()