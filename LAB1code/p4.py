from getpass import getpass

n=1
ans=int(getpass("Player 1, write down your number secretely:"))
while n<=6:
	guess = int(input("Player 2, input your guess: "))
	if guess < ans:
		print("Your guess is too low!")
	elif guess > ans: 
		print("Your guess is too high!")
	else:
		print("You are right after trying for",n,"times. Program ends")
		break
	n += 1
if n>6:
	print("You have tried 6 times and it is still wrong! The answer is %d and program ends."%ans)