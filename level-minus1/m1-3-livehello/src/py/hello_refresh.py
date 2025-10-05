#!usr/bin/python3

import time

try:
    for i in range(0, 100):
        print(f'\rHello {i}', end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    print()