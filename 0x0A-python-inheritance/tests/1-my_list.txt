The ``1-my_list`` module
======================

Using ``MyList``
-------------------

Importing the function from the module:
        >>> MyList = __import__("1-my_list").MyList

Checking for module docstring:
         >>> m = __import__("1-my_list").__doc__
         >>> len(m) > 1
         True

Checking for class docstring:
         >>> c = __import__("1-my_list").MyList.__doc__
         >>> len(c) > 1
         True

Checking for method docstring:
	 >>> mod = __import__("1-my_list").MyList.print_sorted.__doc__
	 >>> len(mod) > 1
	 True

Checking that MyList inherits from list:
	 >>> issubclass(MyList, list)
	 True

Checking for empty list:
	 >>> l = MyList()
	 >>> l.print_sorted()
	 []

Checking that appendng works:
	 >>> l.append(1)
	 >>> l.append(2)
	 >>> l.append(3)
	 >>> l.append(4)
	 >>> print(l)
	 [1, 2, 3, 4]

Checking for list already in correct order:
	 >>> l.print_sorted()
	 [1, 2, 3, 4]

Checking for reversed order list:
	 >>> l = MyList()
	 >>> l.append(4)
	 >>> l.append(3)
	 >>> l.append(2)
	 >>> l.append(1)
	 >>> print(l)
	 [4, 3, 2, 1]
	 >>> l.print_sorted()
	 [1, 2, 3, 4]
	 >>> print(l)
	 [4, 3, 2, 1]

Checking for one negative number:
	 >>> l.append(-1)
	 >>> l.append(5)
	 >>> print(l)
	 [4, 3, 2, 1, -1, 5]
	 >>> l.print_sorted()
	 [-1, 1, 2, 3, 4, 5]
	 >>> print(l)
	 [4, 3, 2, 1, -1, 5]

Checking for all negative numbers:
	 >>> l = MyList()
	 >>> l.append(-10)
	 >>> l.append(-1)
	 >>> l.append(-7)
	 >>> l.append(-2)
	 >>> l.append(-8)
	 >>> print(l)
	 [-10, -1, -7, -2, -8]
	 >>> l.print_sorted()
	 [-10, -8, -7, -2, -1]
	 >>> print(l)
         [-10, -1, -7, -2, -8]

Checking for too many arguments:
	 >>> l.print_sorted(1)
	 Traceback (most recent call last):
	 ...
	 TypeError: print_sorted() takes 1 positional argument but 2 were given
