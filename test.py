from login import basic, basictwostep

class c:
	w = '\033[91m'
	g = '\033[92m'
	y = '\033[93m'
	b = '\033[94m'
	e = '\033[0m'

class grant:
	def yes():
		return f"{c.g}ACCESS GRANTED{c.e}"
	def no():
		return f"{c.w}ACCESS DENIED{c.e}"
	def maybe():
		return f"{c.y}ACCESS PENDING{c.e}"

entry = input(f"{c.b}Please enter the number (1-2): {c.e}")
if entry == "1":
	maint = basic("test")

	if maint == False:
		print(grant.no())
	elif maint == True:
		print(grant.yes())
elif entry == "2":
	maint = basictwostep("test", "pass", "two", "step")
	if maint == 0:
		print(grant.no())
	elif maint == 1:
		print(grant.maybe())
	elif maint == 2:
		print(grant.yes())
