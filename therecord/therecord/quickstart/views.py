from django.http import JsonResponse
import requests, json, os, fileinput
from django.http import HttpResponse, HttpRequest


def extract(request):
    name = []
    items = []
    local_json_file = 'data.json'
    
    content = requests.get('http://therecord.co/feed.json')
    if content.status_code == 200:
        # json = r.json()
        values = json.loads(content.content)
        for criteria in values['items']:
            title = criteria['title']
            name.append((title.split('-')[1]).strip())
        
        ### Create local file
        with open(local_json_file, 'w') as json_file:
            json.dump(values, json_file, indent=4)
        
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

        return HttpResponse(json.dumps(json_decoded))
    
    return HttpResponse('Cannot Extract content')