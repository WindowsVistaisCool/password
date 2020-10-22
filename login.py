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

def basictwostep(main1=None, two1=None, main2=None, two2=None, main3=None, two3=None):
	if main1 is None:
		return 0
	pw1 = [main1]
	if two1 is None:
		two1 = main1
	pw2 = [two1]
	if main2 is not None:
		pw1.append(main2)
		if two2 is None:
			two2 = main2
		pw2.append(two2)
	if main3 is not None:
		pw1.append(main3)
		if two3 is None:
			two3 = main3
		pw2.append(two3)
	entry = input("Please enter the password: ")
	if entry in pw1:
		print("Password Accepted.")
		entry2 = input("Please enter the 2-auth password: ")
		if entry2 in pw2:
			print("Password Accepted")
			return 2
		else:
			print("Wrong 2-auth password.")
			return 1
	else:
		print("Wrong password")
		return 0
