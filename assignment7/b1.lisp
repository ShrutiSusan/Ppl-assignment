(write-line "Factorial")
(setq a (read))
(setq x a)
(defun factorial(l)
	(if (eq l 1)
	   (setq a 1))
	(if (> l 1)
	   (setq a (* l (factorial (- l 1))))
	)
	a
)
(factorial a)
(format t "The factorial of  ~d is ~d" x a )