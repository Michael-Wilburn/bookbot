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

    
def sort_on(item):
    return item["num"]


def get_sorted_characters(char_counts):
    chars_list = []

    for ch, count in char_counts.items():
        if ch.isalpha():
            chars_list.append({
                "char": ch,
                "num": count
            })

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list