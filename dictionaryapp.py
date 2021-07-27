#Json is {} then a key and a value like a python dictionary. Seperate with a comma
#Words are in "" and definitions are []
#To load json into a python dictionary use the json standard library. 
# >>>import json then >>>data = json.load(open("data.json"))
import json
from difflib import get_close_matches

data = json.load(open("C:/Users/jjt45_000/Desktop/Python/DictionaryApp/data.json"))

def translate(word):    #<<< (word) is a local variable. Has meaning inside the function
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:  #in case user enters words like USA or NATO        
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:   #if the list is greater than 0 words
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])  
        #the [0] returns the first match
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. PLease double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")    #global variable

#To get rid of the [] and , in the output, do the following...
#Sometimes it outputs a list or a string. How to tell the differene with a conditional
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

#  print(translate(word)) <<<without the above  #global variable. Passes this value into value in function def












#Use this vvv to get a similarity between an incorrect string and the closest correct string to it
#import difflib
#from difflib import SequenceMatcher
#SequenceMatcher(None, "rainn", "rain").ratio()
#Another difflib feature is get_close_matches

#   >>> import difflib
#   >>> from difflib import get_close_matches
#   >>> get_close_matches("rainn", ["help", "pyramid","rain"])      (example of getting a match to a word)








