import json

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info['email']['hide'])

data = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name": "Chuck"
    },
    {
        "id" : "002",
        "x" : 7,
        "name" : "Camilo"
    }
]        
'''
info = json.loads(data)
print('user count:', len(info))

for item in info:
    print('name:', item['name'])
    print('id:', item['id'])
    print('atr:', item['x'])
