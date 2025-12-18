def get_num_words(str):
    list_words = str.split()
    return len(list_words)

def get_num_character(s):
    s = s.strip('\ufeff').lower()
    char_dictionary = {}

    for ch in s:
        if ch != ' ':
            char_dictionary[ch] = char_dictionary.get(ch, 0) + 1

    return char_dictionary

    