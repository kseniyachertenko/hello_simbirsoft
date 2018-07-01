from termcolor import colored

# print decorator
def printBlue(func):
	return lambda: print(colored(func(), 'blue'))

@printBlue	
def getMessage():
	return 'Hello, Simbirsoft!'

getMessage()