# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that
# data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a
# place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceUrl + urllib.parse.urlencode({'address': address, 'sensor': 'false'})

    print('retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== fail to retrieve =====')
        print(data)
        continue

    print(js['results'][0]['place_id'])