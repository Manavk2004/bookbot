import string

def txt_from_book(text):
    number_of_words = text.split()
    num_words = len(number_of_words)
    return num_words

def num_of_char(text):
    lower_case = text.lower()
    dict = {}
    alphabet = list(string.ascii_lowercase)
    for i in lower_case:
        if i in alphabet:
            if i not in dict:
                dict[i] = 1
                continue
            dict[i] += 1
    return dict

def sort_on(d):
    return d["num"]

def sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

