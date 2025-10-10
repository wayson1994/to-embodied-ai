#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

# bytes
# bytes is byte sequence
a = bytes("hello", encoding="utf-8") # default : utf-8
print(a) # b'hello'
print(a[0]) # 104 (ASCII h)
print(a[0:4]) # hell
# a = bytes("hello") just makes the string "hello" into bytes.
# print(a): prints the entire bytes object.
# print(a[0]): prints a single byte as an integer, which is the ASCII value of 'h', is 104.
# print(a[0:4]):slices the bytes object and prints the first four bytes, b'hell'
b = b"hello"
if b[0] == ord("h") :
    print("The first element is 'h'")
# ord() return ASCII
