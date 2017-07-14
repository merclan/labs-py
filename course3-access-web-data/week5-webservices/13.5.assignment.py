# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_6176.xml (Sum ends with 51)
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format and Approach

import xml.etree.ElementTree as ET
from urllib.request import urlopen


address = input('Enter location: ')
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_6176.xml'

print('Retrieving', address)
data = urlopen(address).read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

lst = tree.findall('.//count')
print('Count:', len(lst))
total = 0
print(data.decode())
for item in lst:
    total = total + int(item.find('.').text)

print('Sum:', total)