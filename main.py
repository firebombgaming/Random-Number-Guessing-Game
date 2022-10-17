import os
import random
import time

os.system("clear")

i = True

num = random.randint(0,100)

print()
print("Welcome To The Number Guessing Game!")
print("Guess a number between 0-100")
print()

time.sleep(2)

os.system("clear")

print()

while - == True:
	print()
	guess_num = float(input("Guess a number: "))
	print()
	if guess_num == num:
		os.system("clear")
		print()
		print("You Guessed the number right!")
		print()
		exit()
    if guess_num < num:
    	print("The number is hHgher!")
    	time.sleep(1)
    	os.system("clear")
    if guess_num > num:
    	print("The number is Lower!")
    	time.sleep(1)
    	os.system("clear")
