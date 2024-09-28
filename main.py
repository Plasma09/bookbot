book_path = "books/frankenstein.txt"
valid_char = list("qwertyuiopasdfghjklzxcvbnm")


def main():
    book = get_book_text(book_path)
    word_count = get_word_count(book)
    character_count = get_character_count(book)
    print(f"--- Beginning the analysis of {book_path} ---")
    print("================================")
    print(f"{word_count} words were found in the document")
    print("================================")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(book):
    words = book.split()
    return len(words)


def get_character_count(book):
    char_dict = {}
    char_list = []
    lower_string = book.lower()
    for char in lower_string:
        if char in valid_char:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    result_list = []
    for char in char_dict:
        count = char_dict[char]
        result_list.append(f"The letter '{char}' was found {count} times")
    

    return "\n".join(result_list)

main()
