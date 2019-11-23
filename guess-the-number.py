import random

num_rand = random.randint(0,100) # a number between 0 and 99 

cont = 6 # chances
adm = True # for while exit

while adm :
	resp_user = int(input("Guess a number between 0 to 100 > "))
	cont -= 1
	if resp_user > num_rand :
		print("Your number is higher, Try again :(")
		print("You have {} attempts".format(cont))
		if cont == 0 :
			print("Your attempts are over :(\nThe number was {}".format(num_rand))
			adm = False

	elif resp_user < num_rand :
		print("Your number is lower ,try again :(")
		print("You have {} attempts".format(cont))
		if cont == 0 :
			print("Your attempts are over :(\nThe number was {}".format(num_rand))
			adm = False
	
	elif resp_user == num_rand :
		print("############################")
		print("Congratulations! You Won! :D\nThe number was {}.".format(num_rand))
		print("############################")
		adm = False
