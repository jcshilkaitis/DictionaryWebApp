from django.shortcuts import render
import requests
import json
import re

# Create your views here.
def index(request):
    return render(request, 'index.html')
    

def word(request):

    user_input = request.GET['word']  
    pattern = re.compile(r"^[a-zA-Z']*$")
    
    if re.fullmatch(pattern, user_input):
        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + user_input)
        pythoned_json = json.loads(response.text)   
        word = pythoned_json[0]['word']
        #definition = pythoned_json[0]['meanings'][0]['definitions'][0]['definition']
        definition = get_definitions(pythoned_json)        
        result = dict({'word' : word, 'definition': definition})
        return render(request, 'results.html', {'result': result })
    else:
        word = 'Sorry, '+ user_input + ' was not found.'
        definition = ''
        result = dict({'word' : word, 'definition': definition})
        return render(request, 'results.html', {'result': result })
        
def get_definitions(json):
    definition = []
    i = 0
    while i < 3:
        try:
            for (k, v) in json[0]['meanings'][i]['definitions'][0].items():
                if k == "definition":
                    definition.append(v)
                    # print(k,v)
                    # print(i)
                    i += 1
        except IndexError:
            break
    return definition