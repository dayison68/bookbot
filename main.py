#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from stats import word_count 
from stats import character_counts
from stats import sorted_char_count

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()

    return book_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    #book_text = get_book_text("./books/frankenstein.txt")
    book_text = get_book_text(book_path)
    wordc = word_count(book_text)
    characters = character_counts(book_text)
    sorted_characters = sorted_char_count(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordc} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['character']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
