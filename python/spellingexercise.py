words = ["color", "color", "colour", "amok", "amok", "amuck", "adviser", "advisor", "adviser", "pepper" ]
canonical_spellings = ["color", "amuck", "adviser", "pepper"]

#create dictionary to pair incorrect and correct spellings
mappings = {"colour": "color", "amok": "amuck", "advisor": "adviser" }

#create empty list
new_list = []

#loop over the list of words
for word in words:
    if word in mappings:
    #if word is misspelled do something
    #correct spelling
        corrected_word = mappings[word]
    #add to new_list
        new_list.append(corrected_word)
    else:
    #if word is correct add to new_list
        new_list.append(word)

print(new_list)
