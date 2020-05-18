(write-line "FACTORIAL")
(setq x (read))
(setq b x)
(setq factorial 1)
(loop
	(setq factorial ( * factorial x))
	(setq x (- x 1))
	(when(< x 2)(return x))
)

(format t "Factorial of ~d is ~d" b factorial)