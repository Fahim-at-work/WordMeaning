import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yes_no = input("Did you mean {0} instead? Enter Y if yes or N for no: ".format(get_close_matches(w,data.keys())[0]))
        yes_no = yes_no.lower()
        if yes_no == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yes_no == 'n':
            return "The word doesn't exist, please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "This word doesn't exist, please try again."

word = input("Enter a word to find the meaning: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print('\n' + i)
else:
    print(output)