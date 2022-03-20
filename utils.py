from strings import some_words
def convert_to_list(s):
    """
       Converts a multiline string into a list of key-value pairs separated by a colon.
    """
    import re
    pattern_one = r'\t'
    pattern_two = r'\n'
    pattern_three= r'\w+:\w+'
    s = re.sub(pattern_one,':',s)
    s = re.sub(pattern_two,'',s)
    l = re.findall(pattern_three,s)
    return l
def split_join_and_form_dict(l):
    """Takes in a list of key-value pair of strings and converts it into dictionary.

    Args:
        list/array: key-value pair of strings.

    Returns:
        dictionary: A dictionary of key-value pairs.
    """
    myDict = dict() 
    for words in l:
        w = words.split(':')
        myDict[w[0]] = w[1]
    return myDict
def english_to_french(word):
    """
    Takes in an English word and gives the French equivalent.

    Args:
        word (string): Any valid string.

    Returns:
        string: A string of the translated word. 
    """
    for key,value in dictionary.items():
        if word == value:
            return key
    return 'does not exist in this dictionary.'

def french_to_english(word):
    """
    Takes in a French word and gives the English equivalent.

    Args:
        word (string): Any valid string.

    Returns:
        string: A string of the translated word. 
    """
    if word in dictionary:
        return dictionary[word]
    else:
        return 'n"existe pas dans cette dictionnaire.'
dictionary = convert_to_list(some_words)
dictionary = split_join_and_form_dict(dictionary)
