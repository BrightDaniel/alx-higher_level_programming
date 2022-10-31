#!/usr/bin/python3
"""
function that appends a string
"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
