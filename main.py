from stats import *

def main():
    print("============ BOOKBOT ============")
    
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
      
    character_count = no_of_times_character_appears(book_text)
    sorted = sort_char(character_count)
    
    print("--------- Character Count -------")
    for char in sorted:
        print(f"{char[0]}: {char[1]}")

main()