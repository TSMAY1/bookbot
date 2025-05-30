def number_of_words(book_text):
        word_list = book_text.split()
        word_count = len(word_list)
        return word_count

def amount_by_character(book_text):
        characters = {}
        for i in book_text:
            lowercase = i.lower()
            if lowercase not in characters:
                characters[lowercase] = 1
            else: characters[lowercase] += 1
        return characters
        
def sort_on(characters):
    return characters["num"]

def create_report(characters):
    sorted_list = []
    for character, num in characters.items():
        if character.isalpha():
            sorted_list.append({"char": character, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
  
     


            