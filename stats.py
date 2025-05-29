def number_of_words(book_text):
        word_list = book_text.split()
        word_count = len(word_list)
        print(f"{word_count} words found in the document")

def amount_by_character(book_text):
        characters = {}
        for i in book_text:
            lowercase = i.lower()
            if lowercase not in characters:
                characters[lowercase] = 1
            else: characters[lowercase] += 1
        return characters
        


            