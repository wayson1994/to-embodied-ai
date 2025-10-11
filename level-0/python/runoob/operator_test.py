#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

# arithmetic operator
# + - * / // % **
print(1 + 1) # 2
print(1 - 1) # 0
print(3 * 2) # 6
print(7 / 3) # 2.3333333333333335 precision issues of float
print(0.1 + 0.2)  # 0.30000000000000004 precision issues of float
print(7 // 3) # 2 divisible
print(2 ** 3) # 8 power

# compare operator
# == != > < >= <=
print(1 == 2) # False
print(1 != 2) # True
print(1 > 2) # False
print(1 < 2) # True
print(1 >= 2) # False
print(1 <= 2) # True

# assginment operator
# = += -= *= /= %= **= //= :=
a = 5
b = a
print(b) # 5
b += 7
print(b) # 12
b *= 3
print(b) # 36
b /= 4
print(b) # 9.0 float
b //= 4
print(b) # 2.0
b **= 3
print(b) # 8.0

# before 3.8
str1 = "wayson"
if len(str1) > 3 :
    c = len(str1)
    print(f"List is too long ({c} elements, expected <= 3)")

# after 3.8 (:=)
if (d := len(str1)) > 3 :
    print(f"List is too long ({d} elements, expected <= 3)")

# bitwise operator
# & | ^ ~ << >>
b_a = 0b0011_1100 # 60
b_b = 0b0000_1110 # 14

print(format(b_a & b_b, '08b')) # 00001100
print(format(b_a | b_b, '08b')) # 00111110
print(format(b_a ^ b_b, '08b')) # 00110010
print(format(~b_a, '08b')) # -0111101 ~x == -x - 1, ~b_a == -60 - 1 == -61 == 10111101
print(format(b_a >> 2, '08b')) # 00001111
print(format(b_a << 2, '08b')) # 11110000

# logical operator
# and or not
a = 10
b = 0
print(a and b) # 0, means False
print(a or b) # 10, means True
print(not(a and b)) # True, 'not' will output True or False

# membership operator
names = {'wayson', 'jack', 'lee'}
print('wayson' in names) # True
print('icy' not in names) # True

# identity operator
class A :
    def __init__(self, name, age):
        self._name = name
        self._age = age
c_a = A('wayson', 10)
c_b = A('jack', 20)
listx = {'wayson', 10}
print(c_a is c_b)  # False
c_b = c_a
print(c_a is c_b)  # True
print(c_a is not listx) # True