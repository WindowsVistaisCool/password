def basic(password1, password2=None, password3=None):
	pw = [password1]
	if password2 is not None:
		pw.append(password2)
	if password3 is not None:
		pw.append(password3)
	invalid = 0
	entry = input("Please enter the password: ")
	if entry in pw:
		print("Password accepted")
		return True
	else:
		if invalid > 4:
			print("Too many incorrect answers reached!\nPlease try again later")
			invalid -=1
		else:
			print("Incorrect Password!")
			invalid += 1
		return False
