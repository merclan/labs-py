# ^     Matches the beginning of a line
# $     Matches the end of the line
# .	    Matches any character
# \s    Matches whitespace
# \S	Matches any non-whitespace character
# *	    Repeats a character zero or more times
# *?	Repeats a character zero or more times (non-greedy)
# +	    Repeats a character one or more times
# +?	Repeats a character one or more times (non-greedy)
# [aeiou]	Matches a single character in the listed set
# [^XYZ]	Matches a single character not in the listed set
# [a-z0-9]	The set of characters can include a range
# \ scape character
#


import re

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print('numbers', y)

# greedy matching
x = 'From: using the: greedy matching'

# greedy
y = re.findall('^F.+:', x)

# non-greedy
z = re.findall('^F.+?:', x)
print('gredy', y)
print('non-greedy', z)

x = 'from stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print('matching', y)
# extracting only what I need even though the match is different
z = re.findall('^from (\S+@\S+)', x)
print('extracting', z)

# extracting domain
y = re.findall('@([^ ]*)', x)
print('extracting domain', y)

hand = open("../files/mbox-short.txt")
numList = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numList.append(num)
print('Max: ', max(numList))