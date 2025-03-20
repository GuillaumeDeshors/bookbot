def count_words(text):
    word_count = len(text.split())
    return word_count

def count_symbols(text):
    text = text.lower()
    dictionnary = {}
    for letter in text:
        dictionnary[letter] = 1 + dictionnary.get(letter, 0)
    return dictionnary

def sort_on(dict):
    return dict["count"]

def report(dictionnary):
    pairs = []
    for key, value in dictionnary.items():
        pairs.append({"character": key, "count": value})
    
    pairs.sort(reverse=True, key=sort_on)

    return pairs
