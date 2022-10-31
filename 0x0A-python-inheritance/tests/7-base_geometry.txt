The ``7-base_geometry`` module
======================

Using ``BaseGeometry``
-------------------

Importing the function from the module:
        >>> BG = __import__("7-base_geometry").BaseGeometry

Checking for module docstring:
         >>> m = __import__("7-base_geometry").__doc__
         >>> len(m) > 1
         True

Checking for class docstring:
         >>> c = __import__("7-base_geometry").BaseGeometry.__doc__
         >>> len(c) > 1
         True

Checking for method docstring:
	 >>> mod1 = __import__("7-base_geometry").BaseGeometry.area.__doc__
	 >>> len(mod1) > 1
	 True
	 >>> mod2 = __import__("7-base_geometry").BaseGeometry.integer_validator.__doc__
         >>> len(mod2) > 1
         True

Checking for area failure:
	 >>> b = BG()
	 >>> b.area()
	 Traceback (most recent call last):
	 ...
	 Exception: area() is not implemented

Checking too many arguments for area:
	 >>> b.area(1)
	 Traceback (most recent call last):
         ...
	 TypeError: area() takes 1 positional argument but 2 were given

Checking integer validator for passing integer:
	 >>> b.integer_validator("integer", 1)

Checking for integer == 0:
	 >>> b.integer_validator("integer", 0)
	 Traceback (most recent call last):
         ...
         ValueError: integer must be greater than 0

Checking for integer < 0;
	 >>> b.integer_validator("integer", -5)
	 Traceback (most recent call last):
         ...
         ValueError: integer must be greater than 0

Checking for non-integer types:
	 >>> b.integer_validator("bool", True)
	 Traceback (most recent call last):
         ...
         TypeError: bool must be an integer
	 >>> b.integer_validator("float", 1.5)
         Traceback (most recent call last):
         ...
         TypeError: float must be an integer
	 >>> b.integer_validator("complex", complex(1, 1))
         Traceback (most recent call last):
         ...
         TypeError: complex must be an integer
	 >>> b.integer_validator("string", "hello")
         Traceback (most recent call last):
         ...
         TypeError: string must be an integer
	 >>> b.integer_validator("tuple", (1, 2))
         Traceback (most recent call last):
         ...
         TypeError: tuple must be an integer
	 >>> b.integer_validator("list", [1, 2, 3])
	 Traceback (most recent call last):
         ...
         TypeError: list must be an integer
	 >>> b.integer_validator("dict", {"key": "value"})
         Traceback (most recent call last):
         ...
         TypeError: dict must be an integer
	 >>> b.integer_validator("set", {"hello", "world"})
         Traceback (most recent call last):
         ...
         TypeError: set must be an integer
	 >>> b.integer_validator("frozenset", frozenset(["hello", "world"]))
         Traceback (most recent call last):
         ...
         TypeError: frozenset must be an integer
	 >>> b.integer_validator("bytes", b"bytes")
         Traceback (most recent call last):
         ...
         TypeError: bytes must be an integer
	 >>> b.integer_validator("bytearrays", bytearray(b"bytes"))
         Traceback (most recent call last):
         ...
         TypeError: bytearrays must be an integer

Checking for no arguments to integer_validator:
	 >>> b.integer_validator()
	 Traceback (most recent call last):
         ...
	 TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

Checking for only 1 argument to integer_validator:
	 >>> b.integer_validator("integer")
	 Traceback (most recent call last):
         ...
	 TypeError: integer_validator() missing 1 required positional argument: 'value'

Checking for too many arguments:
	 >>> b.integer_validator("integer", 1, 2)
	 Traceback (most recent call last):
         ...
	 TypeError: integer_validator() takes 3 positional arguments but 4 were given
