class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   except:
      try:	
	   raise Networkerror("Bad hostname")
      except Networkerror,e:
	   print e.args   
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"
except SyntaxError:
   print ("We came across a Syntax Error,Please do the necessary changes");
   
