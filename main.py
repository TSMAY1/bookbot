def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    return book_text

def number_of_words(book_text):
        word_list = book_text.split()
        word_count = len(word_list)
        print(f"{word_count} words found in the document")

book_text = main()


number_of_words(book_text)
