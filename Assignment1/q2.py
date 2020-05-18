import random 

string="yes"

while string=="yes":

	print("the Value is")
	value=random.randint(1,6)
	print(value)
	string=input("Roll the dice again?")

