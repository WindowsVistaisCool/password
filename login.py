import json

def main():
	with open('.h.json', 'r') as v:
		x = json.load(v)
	if x["p"] > 2:
		print("Too many bad attempts!\nPlease try again later.")
		with open('.h.json', 'r') as v:
			x = json.load(v)
		x["p"] -= 1
		with open('.h.json', 'w') as v:
			json.dump(x, v, indent=4)
		return 0
	else:
		with open('p.json', 'r') as v:
			x = json.load(v)
		passwords = x
		entry = input("Please enter the password: ")
		if entry in passwords:
			print("Password accepted")
			return 1
		else:
			with open('.h.json', 'r') as v:
				x = json.load(v)
			if x["p"] > 5:
				print("Too many invalid attempts reached!")
				return 0
			else:
				x["p"] += 1
				with open('.h.json', 'w') as v:
					json.dump(x, v, indent=4)
				print("Incorrect Password!")
				main()
main()
