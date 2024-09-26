def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counted_words = count_words(text)
    counted_chars = count_chars(text)
    real_char_list = make_dict_into_list(counted_chars)
    real_char_list.sort(reverse=True, key=sort_on)
    breakdown(book_path, counted_words, real_char_list)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def count_chars(text):
    lower_case_text = text.lower()
    char_list = list(lower_case_text)
    char_total = {}
    for char in char_list:
        if char in char_total:
            char_total[char] += 1
        else:
            char_total[char] = 1
    return char_total


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]


def make_dict_into_list(dict):
    dictionary_list = []
    for char, count in dict.items():
        if char.isalpha() == True:
            transition_dict = {"char": char, "count" : count}
            dictionary_list.append(transition_dict)
    return dictionary_list



def breakdown(name, words, characters):
    print(f"--- Begin report of {name} ---")
    print(f"There are {words} in this document")
    print("")
    for chars in characters:
        print(f"The '{chars["char"]}' character was found {chars["count"]} times")
    print("--- End Report ---")
    

main()