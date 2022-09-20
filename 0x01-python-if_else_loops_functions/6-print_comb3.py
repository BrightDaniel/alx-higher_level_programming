#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=', ')
print("{:d}{:d}".format(i + 1, j))
