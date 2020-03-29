#!/home/federico/anaconda3/bin/python
"""reducer.py"""

import sys

current_year = None
current_max = float('-inf')
year = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    year, degrees = line.split('\t')

    # convert year and degrees (currently strings) to int
    try:
        year = int(year)
        # degrees in dataset are multiplied by 10
        degrees = int(degrees) / 10
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_year == year:
        current_max = max(current_max, degrees)
    else:
        if current_year:
            print(f'{current_year}\t{current_max}')
        current_year = year
        current_max = degrees

if current_year == year:
    print(f'{current_year}\t{current_max}')
