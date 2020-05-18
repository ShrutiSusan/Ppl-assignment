l=int(input("Enter a lower range"))
u=int(input("Enter a upper range"))
l1=[]
for i in range(l,u+1):
	temp=i
	sum1=0
	while temp>0:
		last=temp%10
		temp=(temp//10)  
		sum1=sum1+last*last*last
	if (sum1==i):
		l1.append(i)
print(l1)
