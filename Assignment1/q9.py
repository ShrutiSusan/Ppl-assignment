i=1
count=0
rec=0
number=1
count1=0
while (count1<11):
	count=0
	rec=0
	for j in range(1,number+1):
		if(number %j==0):
			count=count+1
			rec=rec+1/j
	
	result=count/rec
	
	number=number+1
	if(result-int(result)==0.00000000000):
		print(number-1)
		count1=count1+1
	
