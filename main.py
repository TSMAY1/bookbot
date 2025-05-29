def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    return book_text

from stats import number_of_words

book_text = main()

number_of_words(book_text)

from stats import amount_by_character

characters = amount_by_character(book_text)
print(characters)