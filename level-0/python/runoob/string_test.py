#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

str1 = "wayson_studio"

print("=== basics of string ===")

print(str1[0])  # w
print(str1[:])  # wayson_studio equals str1
print(str1[3:])  # son_studio
print(str1[:6])  # wayson
print(str1[3:6])  # son
print(str1[3:8:2])  # sns
print(str1[3:8:2] + "python study")  # snspython study
print("wayson \
      studio")  # wayson       studio  with 7 space

print("===== escape character =====")

print("\\ \' \" \n ")  # \ ' " (\n is line feed)
print("\a")  # bell
print("hello \bworld")  # helloworld
print("hello\vhello\tworld")
print("hello\rworld \\r will replace the word")  # world \r will replace the word
print("\141")  # a octal of 97, is 64 + 32 + 1 = 1*8² + 4*8¹ + 1*8⁰=141
print("\x61")  # a hexadeciaml of 97, is 96 + 1 = 6*16¹ + 1*16⁰ = 61

print("===== operator =====")
print("Hello" + "World")  # HelloWorld
print("Hello" * 2)  # HelloHello output 2 times
print('w' in str1)  # True
print('f' not in str1)  # True
print(r"C:user\wayson\wayson1994\to-embodied-ai\level-0\python\runoob")  # raw string, no escape processing

print("===== string formatting =====")
# don't use % or str.format anymore —— just learn f-string
# unless you're stuck supporting legacy versions —— then study str.format
# the % formatting style has been officiall marked as "legacy"