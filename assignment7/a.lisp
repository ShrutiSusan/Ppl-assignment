(setf my_array( make-array '(10)))
(setf (aref my_array 0) 43)
(setf (aref my_array 1) 65)
(setf (aref my_array 2) 23)
(setf (aref my_array 3) 43)
(setf (aref my_array 4) 34)
(setf (aref my_array 5) 67)
(setf (aref my_array 6) 65)
(setf (aref my_array 7) 09)
(setf (aref my_array 8) 34)
(setf (aref my_array 9) 11)
(write my_array)
(write-line " Enter the values of x to access between 0 and 10")
(setq b (read))
(setq x (- b 1))
(cond (( < x 10)
(format t "~2d is ~2d element of the list" (aref my_array x) b))

( t(write "Enter a valid entry val")))






 


