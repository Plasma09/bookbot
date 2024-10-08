# Declaring variables for the doc path & the list of alphabetical characters
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


# 1- Convert the text into lower case
# 2- Loop into the text comparing it to the valid_char list
# 3- Assign all valid characters to char_dict and increment it's number
# 4- Convert char_dict into a list of dictionnaries & sort alphabetically
# 5- Return the list ordered with each character on a new line
def get_character_count(book):
    char_dict = {}
    lower_string = book.lower()
    for char in lower_string:
        if char in valid_char:
            char_dict[char] = char_dict.get(char, 0) + 1

    result_list = [
        f"The letter '{char}' was found {count} times"
        for char, count in char_dict.items()
    ]
    result_list.sort(key=lambda text: text.split()[2])

    return "\n".join(result_list)


main()
