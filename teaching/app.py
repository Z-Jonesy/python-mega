import difflib
from difflib import get_close_matches
import json
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        a = input("Did you mean %s ?  Y/N " % get_close_matches(w, data.keys())[0])
        a = a.lower()
        if a == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif a == "n":
            return
        else:
            return


    else:
        return "The word does not exists "

w = input("Enter a word: ")

output = translate(w)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
