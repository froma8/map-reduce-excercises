#!/home/federico/anaconda3/bin/python
"""mapper.py"""

import sys

# The dataset has 9999 value for missing value of temperature
MISSING = 9999

# Data comes from standard input
for line in sys.stdin:
    line = line.strip()

    # In the dataset year is in that position
    year = line[15:19]
    # While temperature can have or not the plus symbol, in those positions
    degrees = line[87] == '+' and line[88:92] or line[87:92]

    # If the value is not the missing value, then print it for reducer
    degrees != MISSING and print(f'{year}\t{degrees}')
