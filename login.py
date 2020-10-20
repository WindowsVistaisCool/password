import json

def main(password1, password2=None, password3=None):
	pw = [password1]
	if password2 is not None:
		pw.append(password2)
	if password3 is not None:
		pw.append(password3)
	with open('.h.json', 'r') as v:
		x = json.load(v)
	if x["p"] > 2:
		print("Too many bad attempts!\nPlease try again later.")
		with open('.h.json', 'r') as v:
			x = json.load(v)
		x["p"] -= 1
		with open('.h.json', 'w') as v:
			json.dump(x, v, indent=4)
		return False
	else:
		entry = input("Please enter the password: ")
		if entry in pw:
			with open(".h.json", "r") as v:
				x = json.load(v)
			x["p"] = 0
			with open(".h.json", "w") as v:
				json.dump(x, v, indent=4)
			print("Password accepted")
			return True
		else:
			with open('.h.json', 'r') as v:
				x = json.load(v)
			if x["p"] > 5:
				print("Too many invalid attempts reached!")
				return True
			else:
				x["p"] += 1
				with open('.h.json', 'w') as v:
					json.dump(x, v, indent=4)
				print("Incorrect Password!")
				main(password1, password2, password3)
