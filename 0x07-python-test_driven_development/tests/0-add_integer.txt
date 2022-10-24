The ``0-add_integer`` module
======================

Using ``add_integer``
-------------------

Importing the function from the module:
	>>> add_integer = __import__("0-add_integer").add_integer

Checking for module docstring:
	 >>> m = __import__("0-add_integer").__doc__
	 >>> len(m) > 1
	 True

Checking for function docstring:
	 >>> f = __import__("0-add_integer").add_integer.__doc__
         >>> len(f) > 1
         True

Checking regular addition:
	 >>> add_integer(2, 3)
	 5

Checking positive with negative:
	 >>> add_integer(2, -4)
	 -2

Checking negative with positive:
	 >>> add_integer(-6, 8)
	 2

Checking addition over multiple values:
	 >>> [add_integer(i, i ** 2) for i in range(6)]
	 [0, 2, 6, 12, 20, 30]

Checking float with int:
	 >>> add_integer(2.1, 4)
	 6

Checking int with float:
	 >>> add_integer(5, 7.8)
	 12

Checking both float:
	 >>> add_integer(2.45, 3.1)
	 5

Checking for passed NaN:
	 >>> add_integer(1, float('nan'))
	 Traceback (most recent call last):
	 ...
	 ValueError: cannot convert float NaN to integer

Checking for passed inf:
	 >>> add_integer(1, float('inf'))
	 Traceback (most recent call last):
	 ...
	 OverflowError: cannot convert float infinity to integer

Checking super long int:
	 >>> add_integer(999999999999999999999999999999, 1)
	 1000000000000000000000000000000

Checking non-number with number:
	 >>> add_integer([1], 2)
	 Traceback (most recent call last):
	 ...
	 TypeError: a must be an integer

Checking number with non-number:
	 >>> add_integer(3, "2")
	 Traceback (most recent call last):
	 ...
	 TypeError: b must be an integer

Checking non-number with non-number:
	 >>> add_integer((2,), {"key": "value"})
         Traceback (most recent call last):
         ...
         TypeError: a must be an integer

Checking bool with number:
	 >>> add_integer(True, 1)
	 Traceback (most recent call last):
         ...
         TypeError: a must be an integer

Checking number with bool:
	 >>> add_integer(0, False)
         Traceback (most recent call last):
         ...
         TypeError: b must be an integer

Checking no args:
	 >>> add_integer()
	 Traceback (most recent call last):
	 ...
	 TypeError: add_integer() missing 2 required positional arguments: 'a' and 'b'

Checking one arg:
	 >>> add_integer(1)
	 Traceback (most recent call last):
         ...
	 TypeError: add_integer() missing 1 required positional argument: 'b'

Checking more than 2 args:
	 >>> add_integer(1, 2, 3)
         Traceback (most recent call last):
         ...
         TypeError: add_integer() takes 2 positional arguments but 3 were given
