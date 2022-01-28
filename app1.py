def translate(word):
    word=word.lower()
    if word in data:
       return data[word]
    elif len(get_close_matches(word, data.keys())) >0:
       q= input ("did you mean %a instead? Press Y for yes and N for no  "%get_close_matches(word,data.keys()) [0])
       if   q=="Y":
           return data[get_close_matches(word,data.keys()) [0]]
       elif q=="N":
            return "your entry doesn't match any word "
       else:
           return "entry not found"

    else:
        return "can't find the word, please recheck it"
import json
from difflib import get_close_matches
data=json.load(open("data.json"))
word=input("enter the word:  ")

output= translate(word)
if type(output) == list:
    for item in output:
        print (item)
else:
    print(output)
