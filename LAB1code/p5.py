boo=True
pal=input("Please input a palindrome: ").lower()
while boo:
	reversePal = pal[::-1]
	if pal != reversePal:
		pal = input("No, you must input a palindrome: ").lower()
	else:
		boo = False
print("Welcome to the wonderland!")
