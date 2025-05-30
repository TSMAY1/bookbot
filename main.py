import sys
from stats import number_of_words
from stats import amount_by_character
from stats import create_report


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    return book_text, path_to_file



book_text, path_to_file = main()

word_count = number_of_words(book_text)



characters = amount_by_character(book_text)



report = create_report(characters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}")
print("----------- Word Count ----------")


print(f"Found {word_count} total words")

print("--------- Character Count -------")

for item in report:
    print(f"{item["char"]}: {item["num"]}")

print("============= END ===============")