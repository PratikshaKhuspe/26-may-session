from random import randint

dice=randint(1,6)
guess=rad_int(input('Guess the number:'))

if guess==dice:
	print("Wohoo you got lucky")
else:
	print("Better luck next time.The number was %d")
