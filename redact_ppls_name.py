
url = "http://therecord.co/feed.json"
name = []
local_json_file = 'data.json'
import requests, json, os, fileinput

content = requests.get(url)
values = json.loads(content.content)

### Get list of ppls names:
for criteria in values['items']:
    title = criteria['title']
    name.append((title.split('-')[1]).strip())

### Create local file
with open(local_json_file, 'w') as json_file:
    json.dump(values, json_file, indent=4)

### Remove all name of peoples
for user in name:
    with fileinput.FileInput(local_json_file, inplace=True) as file:
        for line in file:
            print(line.replace(user, ""), end='')

### Add more field to JSON file     
with open(local_json_file) as json_file:
    json_decoded = json.load(json_file)

json_decoded['Custom_field'] = 'This file has been redacted',

with open(local_json_file, 'w') as json_file:
    json.dump(json_decoded, json_file, indent=4)
