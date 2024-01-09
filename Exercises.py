############
# Exercice 1
############

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized.
# The next words should be always capitalized.
# Examples #

# "the-stealth-Warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    new_text = text.replace("-","_").split("_")
    result = [new_text[0]]
    
    for word in new_text[1:]:
        result.append(word[0].upper()+word[1:])
        
    return "".join(result)

############
# Exercice 2
############

# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new_string = []
    for letter in string_:
        if letter not in vowels:
            new_string.append(letter)
    string_ = "".join(new_string)
    return string_

