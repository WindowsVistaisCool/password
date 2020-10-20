from login import main

class c:
	w = '\033[91m'
	g = '\033[92m'
	e = '\033[0m'

maint = main("test")

if maint == False:
	print(f"{c.w}ACCESS DENIED{c.e}")
elif maint == True:
	print(f"{c.g}ACCESS GRANTED{c.e}")
