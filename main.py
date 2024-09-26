def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counted_words = count_words(text)
    counted_chars = count_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {counted_words} in this document")
    print("")
    for chars in counted_chars:
        print(f"The '{chars}' character was found {counted_chars[chars]} times")
    print("--- End Report ---")

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


    

main()