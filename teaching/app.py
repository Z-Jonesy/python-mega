import json
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exists "

w = input("Enter a word: ")
print(translate(w))
