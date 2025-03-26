def word_count(book_text):
    num_words = 0 
    for line in book_text.splitlines():
        words = line.split()
        num_words += len(words)
    #print(f"{num_words} words found in the document")
    return num_words

def character_counts(book_text):
    book_text = book_text.lower()
    characters = {}

    for char in book_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    #print(characters)
    return characters


def sorted_char_count(characters):
    sorted_list = [
            {"character": char, "count": count}
            for char, count in characters.items()
            if char.isalpha()
        ]

    sorted_list.sort(key=lambda item: item["count"], reverse=True)

    return sorted_list
