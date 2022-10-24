The ``3-say_my_name`` module
======================

Using ``say_my_name``
-------------------

Importing the function from the module:
	>>> say_my_name = __import__("3-say_my_name").say_my_name

Checking for module docstring:
	 >>> m = __import__("3-say_my_name").__doc__
	 >>> len(m) > 1
	 True

Checking for function docstring:
	 >>> f = __import__("3-say_my_name").say_my_name.__doc__
         >>> len(f) > 1
         True

Checking for passing None as first name:
	 >>> say_my_name(None, "Hello")
	 Traceback (most recent call last):
         ...
         TypeError: first_name must be a string

Checking for passing None as last name:
	 >>> say_my_name("Hello", None)
	 Traceback (most recent call last):
         ...
         TypeError: last_name must be a string

Checking for wrong type as first name:
         >>> say_my_name(1, "Hello")
         Traceback (most recent call last):
         ...
         TypeError: first_name must be a string

Checking for wrong type as last name:
         >>> say_my_name("Hello", [4])
         Traceback (most recent call last):
         ...
         TypeError: last_name must be a string

Checking for normal use:
	 >>> say_my_name("Hello", "World")
	 My name is Hello World
	 >>> say_my_name("You know nothing", "John Snow")
	 My name is You know nothing John Snow

Checking for 1 arg:
	 >>> say_my_name("Hello")
	 My name is Hello 

Checking for more than 2 args:
	 >>> say_my_name("Hello", "World", "hi")
	 Traceback (most recent call last):
	 ...
	 TypeError: say_my_name() takes from 1 to 2 positional arguments but 3 were given
