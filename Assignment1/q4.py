import random
number=random.randint(1,100)
var=0
flag=0
print("YOU GET ONLY 5 GUESSES!")
while var!=5:
	user=int(input("Enter a number"))
	if (number>user):
		print("The number is greater than what is guessed")
		print("Try Again")
	elif (number<user):
		print("The number is less than what is guessed")
		print("Try Again")
	else:
		print("The number guessed it right")
		flag=1
		break
		
	var=var+1
if( flag==0):
	print("Sorry,the number couldnt be guessed ",number)	
