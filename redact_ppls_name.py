
url = "http://therecord.co/feed.json"
name = []
import requests, json, os

content = requests.get(url)
values = json.loads(content.content)



for criteria in values['items']:
    title = criteria['title']
    name.append((title.split('-')[1]).strip())


# for name in name:
#     transformed_data = json.loads(json.dumps(values).replace(name, ""))
with open('personal.json', 'w') as json_file:
    json.dump(values, json_file, indent=4)
    # for name in name:
    #     transformed_data = json.loads(json.dumps(json_file).replace(name, ""))
    #     json.dump(transformed_data, json_file, indent=4)


#fin = open("personal.json")
#fout = open("personal.json", "w+")

for line in fin:
     print (line)
     for word in name:
         line = line.replace(word, '')
     fout.write(line)
fin.close()
fout.close()

# for line in values:
#     print (line)
#     for name in name:
#         line = line.replace(name, '')
#     fout.write(line)

