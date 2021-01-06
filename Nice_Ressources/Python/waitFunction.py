"""Useful Functions"""

from time import sleep
def wait(a,b):
	"""Allow the System to be on pause between a and b seconds"""
	# random stops (seconds)
	random_time = randint(a, b)
	#print("Browser sleeps for " + str(random_time) + " seconds")
	sleep(random_time)

