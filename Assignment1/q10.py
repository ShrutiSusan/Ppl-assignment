from math import pow

def gs(a,r):
	
	for i in range(1,11):
		dis=int(a*pow(r,i-1))
		print(dis)
	
#driver code
a=int(input("Enter"))
r=int(input("Enter the common ratio"))
gs(a,r)
