def checkami(a,b):
    s=0
    for k in range(1,a):
    
        if(a%k==0):
        
            s=s+k
     
    if(s==b):
    
        s=0
        for i in range(1,b):
       
            if(b%i==0):
            
                s=s+i
        if(s==a):
            return 1
        else:
            return 0
    return 0
l1=[]   
for i in range(2,100000):
	for j in range(2,100000):
		if(i not in l1):
			if(i!=j):
				boolean=checkami(i,j)
				if (boolean):
					l1.append(i)
					l1.append(j)
					print("(",i,",",j,")")
			else:
				continue
