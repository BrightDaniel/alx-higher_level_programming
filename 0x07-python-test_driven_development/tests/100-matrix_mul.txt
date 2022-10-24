The ``matrix_mul`` module
==========================

Using ``matrix_mul``
---------------------

First import ``matrix_mul`` from the ``matrix_mul`` module:

	>>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Now use it:

	>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
	[[7, 10], [15, 22]]

	>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
	[[13, 16]]
	
	>>> matrix_mul([[1, 2, 3]], [[3, 4, 5], [5, 6, 8], [9, 10, 11]])
	[[40, 46, 54]]

	>>> matrix_mul([[2]], [[7]])
	[[14]]


	>>> matrix_mul(9, [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: m_a must be a list

	>>> matrix_mul([[1, 2], [3, 4]], 9)
	Traceback (most recent call last):
	...
	TypeError: m_b must be a list

	>>> matrix_mul(9, 9)
	Traceback (most recent call last):
	...
	TypeError: m_a must be a list


	>>> matrix_mul([1, 2, 3, 4], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: m_a must be a list of lists

	>>> matrix_mul([[1, 2], [3, 4]], [1, 2, 3, 4])
	Traceback (most recent call last):
	...
	TypeError: m_b must be a list of lists

	>>> matrix_mul([1, 2, 3, 4], [1, 2, 3, 4])
	Traceback (most recent call last):
	...
	TypeError: m_a must be a list of lists


	>>> matrix_mul([], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	ValueError: m_a can't be empty

	>>> matrix_mul([[]], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	ValueError: m_a can't be empty

	>>> matrix_mul([[1, 2], [3, 4]], [])
	Traceback (most recent call last):
	...
	ValueError: m_b can't be empty

	>>> matrix_mul([[1, 2], [3, 4]], [[]])
	Traceback (most recent call last):
	...
	ValueError: m_b can't be empty

	>>> matrix_mul([], [])
	Traceback (most recent call last):
	...
	ValueError: m_a can't be empty

	>>> matrix_mul([[]], [[]])
	Traceback (most recent call last):
	...
	ValueError: m_a can't be empty

	
	>>> matrix_mul([[1, 2], ["Betty", 4]], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: m_a should contain only integers or floats

	>>> matrix_mul([[1, 2], [3, 4]], [[1, "Holberton"], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: m_b should contain only integers or floats

	>>> matrix_mul([[1, 2], [None, 4]], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: m_a should contain only integers or floats


	>>> matrix_mul([[1, 2], [3]], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: each row of m_a must be of the same size

	>>> matrix_mul([[1, 2], [3, 4]], [[1], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: each row of m_b must be of the same size

	>>> matrix_mul([[1, 2], [3]], [[1], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: each row of m_a must be of the same size


	>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4], [5, 6]])
	Traceback (most recent call last):
	...
	ValueError: m_a and m_b can't be multiplied

	>>> matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	ValueError: m_a and m_b can't be multiplied


	>>> matrix_mul()
	Traceback (most recent call last):
	...
	TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

	>>> matrix_mul([[1, 2], [3, 4]])
	Traceback (most recent call last):
	...
	TypeError: matrix_mul() missing 1 required positional argument: 'm_b'
