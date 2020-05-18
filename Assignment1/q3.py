 
      
host_path = r"/etc/hosts"  
redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com"]  
      
while True:  
            with open(host_path,"r+") as fileptr:  
                content = fileptr.read()  
                for website in websites:  
                    if website in content:  
                        pass  
                    else:  
                        fileptr.write(redirect+"        "+website+"\n")  
      	    
       
