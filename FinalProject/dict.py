# User will type a word
# If found, display definition on the screen. More than one definition may exist

# If not found, find a similarly spelled work and suggest it 
# User chooses to accept suggestion by typing y for yes and n for no. (Not case sensitive)
# If n is choosen, display word not found message
# If n nor y are typed, display error message
# If similar word cannot be found, display word not found message

# Dictionary stored in JSON file. User cannot add to the dictionary
# Not in a loop


# Prompt the user for a word to define and print the definition on the screen

# Dictionary Module

import csv
import difflib as dif


def textfile(filename):
    with open(filename, 'r') as f:
        data = csv.reader(f)
    return data


def translate(w, data):
    lower = w.lower()
    # definition = data[lower]
    keys = (data.keys())  # Pulling words from the entire JSON file
    close_matches = dif.get_close_matches(w, keys, n=1)
    # exact_match = dif.get_close_matches(lower, keys, cutoff=1)
    if len(close_matches) <= 0:
        return "No possible matches found in this dictionary."
    elif lower == close_matches[0]:
        # print(len(data[close_matches[0]]))
        # for definition in range(len(data[close_matches[0]])):
        return data[close_matches[0]]
    else:
        answer = input("Did you mean '{}' ? Type y for yes and n for no: ".format(close_matches[0]))
        answer = answer.lower()  # In case caps lock is on
        if answer == "n":
            return "The word does not exist in this dictionary."
        elif answer == "y":
            word = close_matches[0]
            return data.get(word, None), close_matches[0]
            # for definition in data[close_matches[0]]:
            #     return (definition)
        else:
            return ("your answer was not understood.")
    

def typereturn(t):
    if type(t) is int:
        for iterable in range(len(t)):
            return print(t[iterable])
    elif type(t) is str:
        return print(t)
    else:
        return print("Whoops! ", t)

