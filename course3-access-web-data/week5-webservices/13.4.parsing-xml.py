import xml.etree.ElementTree as ET

print('Ex1: ')
data = '''<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 44 56
</phone>
<email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))



print('Ex2: ')
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('user count:', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Attr: ', item.get('x'))