def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    return text
        
def get_text(path):
    with open(path) as f:
        return f.read()

def count_words():
    book = main()
    word_count = len(book.split())
    print("Counting words now...")
    return word_count

def char_count():
    book = main()
    low_book = book.lower()
    chars_dict = {}
    for char in low_book:
        if char.isalpha():
            current_count = chars_dict.get(char, 0)
            chars_dict[char] = current_count + 1
    return chars_dict

def get_report():
    print(f"--- Begin report of books/frankenstein.txt")
    print(count_words())
    print(" ")
    sorted_chars = sorted(char_count().items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_chars:
        print(f"The '{letter}' character was found {count} times")
    print(" ")
    print("--- End report ---")

get_report()