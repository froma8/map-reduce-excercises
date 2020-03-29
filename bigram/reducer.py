#!/home/federico/anaconda3/bin/python
"""reducer.py"""

import sys

current_word = None
current_count = 0
word = None
words = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    couple, count = line.split('\t', 1)

    first, second = couple.split()

    bigram = (first, second)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if bigram in words:
        words[bigram] += count
    else:
        words[bigram] = count

for k, v in words.items():
    print(f'{k}\t{v}')


