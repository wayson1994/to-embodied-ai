#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

counter = 100 # int
miles = 1000.0 # float
name =  "jack" # str

print(counter)
print(miles)
print(name)

# multivariate assignment
a = b = 1
print(a, b)

a, b, c = 1, 2, "jack"
print(a, b, c)

is_active = True

print(type(a)) # <class 'int'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'str'>
print(type(is_active)) # # <class 'bool'>

# number
# int float bool complex
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'bool'>
print(type(d)) # <class 'complex'>

a = 111
print(isinstance(a, int)) # True

# differences between type and isinstance
class A:
    pass
class B(A):
    pass
print(isinstance(A(), A)) # True
print(type(A())) # <class '__main__.A'>
print(isinstance(B(), A)) # True
print(type(B())) # <class '__main__.B'> (not A)

# bool is a subclass of int, True == 1, False == 0
c = True
print(isinstance(c, int)) # True
print(True + 1) # 2
print(False + 1) # 1

# del
del a, b, c, d

# String
str = "wayson"
print(str) # wayson
print(str[0]) # w
print(str[0:-1]) # wayso
print(str[2:5]) # yso
print(str[2: ]) # yson
print(str * 2) # waysonwayon
print(str + "TEST") # waysonTEST

# \
print("way\nson")
# way
# son
print(r"way\nson") # way\nson, adding an 'r' in front of a String indicates a raw string

# and or not
print(True and True) # True
print(False and False) # True
print(True and False) # False

print(True or True) # True
print(True or False) # True
print(False or False) # False

print(not False) # True
print(not True) # False
print(not 1) # False
print(not 0) # True

# compare
print(5 > 3) # True
print(2 == 2) # True
print(7 < 4) # False

# ternary operator
a, b = 10, 20
print(a if a > b else b) # 20

# list
list = [ "asd", "b", "c", 100, 100.1 ]
tinylist = [ 123, "wayson"]

print(list) # [ "asd", "b", "c", 100, 100.1 ]
print(list[0]) # a
print(list[1:3]) # [ "b", "c" ]
print(list[2: ]) # [ "b", "c", 100, 100.1 ]
print(tinylist * 2) # [ 123, "wayson", 123, "wayson" ]
print(list + tinylist) # [ "asd", "b", "c", 100, 100.1, 123, "wayson"]

a = [ 1, 2, 3, 4, 5, 6 ]
a[0] = 9 # [ 9, 2, 3, 4, 5, 6 ]
a[2:5] = [ 13, 14, 15 ] # [ 9, 2, 13, 14, 15, 6 ]
a[2:5] = [] # [9, 2, 6]
print(a)

letters = [ "w", "a", "y", "s", "o", "n", "s", "t", "u", "d", "i", "o"]
print(letters[1:6:2]) # [ "a", "s", "n"]
# from letters[1] to letters[6], step 2
print(letters[-1::-1]) # ['o', 'i', 'd', 'u', 't', 's', 'n', 'o', 's', 'y', 'a', 'w']

# tuple
tuple = ( "abcd", 786, 2.23, "wayson", 70.2)

'''
 differences between list and tuple:
 1.tuple is immutable, list is mutable
 2.tuple use (), list use []
 3.tuple has fewer methods, list has more methods
 4.tuple is faster
 5.tuple is used when data should remain constant, list is used when data may change
 6.tuple is hashable, list is not hashable
'''
 
# set
sites = {"aaa", "bbb", "ccc", "aaa", "ddd", "bbb"}
print(sites) # {'aaa', 'ccc', 'bbb', 'ddd'} 

# function of set:
# 1. remove duplicates
del list # keyword
lists = list(set([ 1, 2, 2, 3, 3, 3 ]))
print(lists) # [ 1, 2, 3 ]
# 2. logical reasoning
set1 = { "Wayson", "Bob", "Jack" }
set2 = { "Wayson", "Ace", "Kenny" }
print(set1 & set2) # {'wayson'}
# 3. faster than list when checking if a value exist (no example)

# dictionary { key : value }
dict = {}
dict["name"] = "wayson"
dict[0] = "hello dictionary"
print(dict) # {'name': 'wayson', 0: 'hello dictionary'}
print(dict["name"]) # wayson
print(dict.keys()) # dict_keys(['name', 0])
print(dict.values()) # dict_values(['wayson', 'hello dictionary'])

# bytes