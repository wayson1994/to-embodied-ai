#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

# implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print(type(num_int)) # <class 'int'>
print(type(num_flo)) # <class 'float'>
print(num_new) # 124.23
print(type(num_new)) # <class 'float'>

print(type(5 / 3)) # both are ints, but the result is a float

# explicit type conversion

#int(x, base=10)
x = int(1)
y = int(1.8)
z = int("3")

print(x) # 1
print(y) # not 1.8, but 1
print(z) # 3

# must be str
x = int('24', 16) # 36
y = int('1101', 2) # 13
z = int('18', 10) # 18

print(x) # 1
print(y) # not 1.8, but 1
print(z) # 3

# str(x)
str_x = str("s1")
str_y = str(2)
str_z = str(3.14)

print(type(str_x)) # <class 'str'>
print(type(str_y)) # <class 'str'>
print(type(str_z)) # <class 'str'>

# TODO 
# repr(x)
# eval(str)
# tuple(s)
# list(s)
# set(s)
# dict(d)
# frozenset(s)
# chr(x)
# ord(x)
# hex(x)
# oct(x)