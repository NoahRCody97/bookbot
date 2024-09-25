def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #count_words(text)
    counted_chars = count_chars(text)
    print(counted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    print(f"There are {word_count} in this document")

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