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