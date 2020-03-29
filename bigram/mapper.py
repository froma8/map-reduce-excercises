#!/home/federico/anaconda3/bin/python
"""mapper.py"""

import sys

for line in sys.stdin:
    words = line.strip().split()
    for i in range(len(words) - 1):
        first, second = words[i:i+2]
        print(f'{first} {second}\t1')
