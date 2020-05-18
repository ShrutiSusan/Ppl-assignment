list1=eval(input("Enter"))
#list1=list1.sort()
list2=[]
i=0
flag=0
for i in range(1,26):
	flag=0
	for j in list1:
		if (i==j):
			flag=1
			break
	if(flag==0):
		list2.append(i)		
	i=i+1
print(list2)
print("are missing from the page numbers list")         
