#!/usr/bin/env python3
# Copyright 2025 Wayson
# SPDX-License-Identifier: MIT
# License text: https://opensource.org/licenses/MIT

# number
# int float complex
var1 = 2
var1 = 2.0
var1 = 1 + 2j

# del
del var1

num = 10  # decimal system
num = 0b0110_0011  # binary system
num = 0o33  # octal
num = 0xFF  # hexadeciaml

del num

# number type conversion
num = 10.0  # float
num = int(num)  # int 10
num = float(num)  # float 10.0
num = complex(1, 1) # complex, 1 + 1j

# functions
# no need to import math
# abs(x)  absolute value
print(abs(-10))
# max(x1, x2, ……)
print(max(10, 20, 40, 30))
# min(x1, x2, ……)
print(min(30, 20, 10, 40))
# round(x[, n])
print(round(70.333))  # 70
print(round(70.333333, 3))  # 70.333
# need to import math
import math
# ceil(x)  rounding up
print(math.ceil(3.14))  # 4
# exp(x)  e to the power of x
print(math.exp(2))  # 7.38905609893065, is equal to e ** 2
# fabs(x)  absolute value of float
print(math.fabs(-7))  # 7.0, float
# floor(x)  rounding down
print(math.floor(3.14))  # 3
# log(x[, base=10])
print(math.log(8, 2))  # 3.0, float
print(math.log(math.e))  # 1.0, float
# log10(x)
print(math.log10(1000))  # 3.0, float
# modf(x) 
print(math.modf(-2.4))  # (-0.3999999999999999, -2.0) floating-point precision issues
# pow(x, y)  x ** y
print(math.pow(2, 3))  # 8.0, float
# sqrt(x)  arithmetic square root
print(math.sqrt(25))  # 5.0, float
# trunc
print(math.trunc(2.9))  # 2
# isfinite
print(math.isfinite(float(math.floor(3.14))))  # return True if it'n not infinity or NaN

print("========== random function ==========")

# random function need to import random
import random
# choice(seq)
print(random.choice(range(10)))
stu_list = ["wayson", "jack", "lee", "mary"]
print(random.choice(stu_list))
# randrange([start], stop[, step])
print(random.randrange(1, 100, 2))
# random [0, 1)
print(random.random())
# seed([x])
random.seed(20)
print(random.random())
# shuffle(lst)
random.shuffle(stu_list)
print(stu_list)
# uniform(x, y)
print(random.uniform(1, 2))

print("========== trigonometric function ==========")

# trigonometric function need to import math
print(math.pi)  # 3.141592653589793
print(math.tau)  # matu.tau = math.pi * 2
print(math.e)  # 2.718281828459045
print(math.sin(0.5 * math.pi))  # 1.0 float
print(math.cos(math.pi))  # -1.0 float
print(math.tan(0))  # 0.0 float
print(math.asin(1))  # 1.5707963267948966 arcsin 
print(math.acos(-1))  # 3.141592653589793 arccos
print(math.atan(1))  # 0.7853981633974483 arctan
print(math.degrees(math.pi))  # 180.0
print(math.radians(180))  # 3.141592653589793

print("===== hyperbolic functions =====")

# hyperbolic functions need to import math
print(math.sinh(2))  # 3.6268604078470186
print(math.cosh(2))  # 3.7621956910836314
print(math.tanh(2))  # 0.9640275800758169

print("===== floating-point comparison =====")

print(math.isclose(0.1 + 0.2, 0.3))  # true 0.1 + 0.2 != 0.3
print(math.copysign(-5, 1))  # 5.0 return the magnitude of first number with the sign of second number

print("===== other =====")

# hypot return the euclidean nrom, sqrt(x² + y²)
print(math.hypot(5, 5))  # 7.0710678118654755 math.hypot(5, 5) = sqrt(5² + 5²) = sqrt(50)
print(math.dist([3, 0], [0, 4]))  # 5.0, distance between p(3, 0) and q(4, 0)
print(math.fsum([0.1, 0.2, 0.3]))  # 0.6 Accurate floating-point sum (reduce rounding error).
print(math.prod([1, 2, 3, 4, 5]))  # 120 Return the product of all elements.
print(math.gcd(16, 12))  # 4 Return the greatest common divisor.
print(math.lcm(7, 31))  # 217 Return the least common multiple.
print(math.isqrt(4))  # 2 Return the integer square root (floor of exact root).
print(math.factorial(5))  # 120 Return n! (n must be int ≥ 0).
print(math.comb(7, 5))  # 21 Return binomial coefficient “n choose k”.