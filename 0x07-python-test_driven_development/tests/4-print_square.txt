The ``4-print_square`` module
======================

Using ``print_square``
-------------------

Importing the function from the module:
	>>> print_square = __import__("4-print_square").print_square

Checking for module docstring:
	 >>> m = __import__("4-print_square").__doc__
	 >>> len(m) > 1
	 True

Checking for function docstring:
	 >>> f = __import__("4-print_square").print_square.__doc__
         >>> len(f) > 1
         True

Checking for no args:
	 >>> print_square()
	 Traceback (most recent call last):
	 ...
	 TypeError: print_square() missing 1 required positional argument: 'size'

Checking for too many args
	 >>> print_square(1, 2)
	 Traceback (most recent call last):
	 ...
	 TypeError: print_square() takes 1 positional argument but 2 were given

Checking for passing None:
	 >>> print_square(None)
	 Traceback (most recent call last):
         ...
         TypeError: size must be an integer

Checking for positive ints:
	 >>> print_square(4)
	 ####
	 ####
	 ####
	 ####
	 >>> print_square(10)
	 ##########
	 ##########
	 ##########
	 ##########
	 ##########
	 ##########
	 ##########
	 ##########
	 ##########
	 ##########
	 >>> print_square(0)
	 >>> print_square(1)
	 #

Checking for negative ints:
	 >>> print_square(-1)
	 Traceback (most recent call last):
         ...
         ValueError: size must be >= 0

Checking for non-number types:
	 >>> print_square((1,))
	 Traceback (most recent call last):
         ...
         TypeError: size must be an integer
	 >>> print_square("3")
	 Traceback (most recent call last):
         ...
         TypeError: size must be an integer
	 >>> print_square(True)
	 Traceback (most recent call last):
         ...
         TypeError: size must be an integer

Checking for non-int number types:
	 >>> print_square(1.0)
	 Traceback (most recent call last):
         ...
         TypeError: size must be an integer
	 >>> print_square(-5.5)
	 Traceback (most recent call last):
         ...
         TypeError: size must be an integer
