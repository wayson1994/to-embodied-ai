#!usr/bin/python3
'''
@file     stopwatch_ns.py
@brief    output 10 pieces of ns
@version  1.0
@author   Wayson
@date     2025.10.5
'''

import time

for i in range(0, 10):
    print(f'ns : {time.perf_counter_ns()}', end='', flush=True)
    print()