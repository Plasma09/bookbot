book_path = "books/frankenstein.txt"
char_list = list("qwertyuiopasdfghjklzxcvbnm")

def main():
    book = get_book_text(book_path)
    word_count = get_word_count(book)
    character_count = get_character_count(book)
    print(f"Word count : {word_count}")
    print(character_count)

def get_word_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(book):
    char_dict = {}
    lower_string = book.lower()
    for char in lower_string:
        if char in char_list:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


main()