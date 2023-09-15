import json
import os
import difflib as dif
os.system('cls')

OutputFile = open("output.txt", mode="r+")
text = OutputFile.read()

with open('data.json', 'r') as f:
    data = json.load(f)
    
word = input('Search definition for: ')
print(word, file=OutputFile)

def translate(w):
    lower = w.lower()
    keys = (data.keys())  # Pulling words from the entire JSON file
    close_matches = dif.get_close_matches(lower, keys, cutoff=0.7)
    if len(close_matches) <= 0:
        print("No possible matches found in this dictionary.", file=OutputFile)
        return "No possible matches found in this dictionary."

    elif lower == close_matches[0]:
        return data[close_matches[0]]
    else:
        print("Did you mean '{}' ? Type y for yes and n for no: ".format(close_matches[0]), file=OutputFile)
        answer = input("Did you mean '{}' ? Type y for yes and n for no: ".format(close_matches[0]))
        print(answer, file=OutputFile)
        answer = answer.lower()  # In case caps lock is on
        if answer == "n":
            print("The word does not exist in this dictionary.", file=OutputFile)
            return "The word does not exist in this dictionary."    
        elif answer == "y":
            return data[close_matches[0]]
        else:
            print("Your answer was not understood.", file=OutputFile)
            return ("Your answer was not understood.")


t = translate(word)

if type(t) is list:

    for iterable in range(len(t)):
        print(t[iterable], file=OutputFile)
        print(t[iterable])
elif type(t) is str:
    print(t)
else:
    print("Whoops! ", t)

os.startfile('output.txt')

