from stats import *

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    character_count = no_of_times_character_appears(book_text)
    print(character_count)

main()