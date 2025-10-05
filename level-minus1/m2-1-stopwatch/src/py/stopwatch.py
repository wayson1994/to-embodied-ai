#!usr/bin/python3
'''
@file     stopwatch.py
@brief    output elapsed 10s
@version  1.0
@author   Wayson
@date     2025.10.5
'''

import time

for i in range(0, 10):
    print(f'elapsed : {i + 1} s', end='', flush=True)
    print()
    time.sleep(1)