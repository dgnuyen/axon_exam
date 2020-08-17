
url = "http://therecord.co/feed.json"
name = []
import requests, json, os, fileinput

content = requests.get(url)
values = json.loads(content.content)



for criteria in values['items']:
    title = criteria['title']
    name.append((title.split('-')[1]).strip())



with open('personal.json', 'w') as json_file:
    json.dump(values, json_file, indent=4)


for user in name:
    with fileinput.FileInput('personal.json', inplace=True) as file:
        for line in file:
            print(line.replace(user, ""), end='')



