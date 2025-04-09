def num_of_words(words):
    word_list = words.split()
    num_words = len(word_list)
    return num_words

def num_of_characters(letters):
    updated_string = letters.lower()
    letter_dict = {}
    for i in updated_string:
        if i.isalpha():
            if i in letter_dict:
                letter_dict[i] += 1
            else:
                letter_dict[i] = 1
    return letter_dict

def sorted_characters(jumbled):
    character_list = []
    for letter, count in jumbled.items():
        character_list.append({'character': letter, 'count': count})
    sorted_dict = sorted(character_list, reverse=True, key=lambda x: x['count'])
    return sorted_dict
