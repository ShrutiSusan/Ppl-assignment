def lu(mat,n):
	l=[[0 for x in range(n)] for y in range(n)]
	u=[[0 for x in range(n)] for y in range(n)]
	#upper decomposition
	for i in range(n):
		for k in range(i,n):
			sum1=0
			for j in range(i):
				sum1=sum1+(l[i][j] *u[j][k])
			u[i][k]= int(mat[i][k]-sum1)
	#lower decomposition
	
		for k in range(i,n):
			if(i==k):
				l[i][i]=1
			else:
				sum1=0
				for j in range(i):
					sum1=sum1 + (l[k][j] * u[j][i])
				l[k][i]= int((mat[k][i]-sum1)/u[i][i])
	print("Lower and Upper Matrices")
	for i in range(n):
		
		for j in range(n):
			print(l[i][j],end="\t")
		for j in range(n):
			print(u[i][j],end="\t")
		
		print("\n")
		
A=[[0 for x in range (3)]for y in range(3)]
for i in range(3):
	for j in range(3):
		A[i][j]=int(input("Enter"))		
lu(A, 3)
