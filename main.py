import sys
from stats import *

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    
    book_path = sys.argv[1]
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