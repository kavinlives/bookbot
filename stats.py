def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def no_of_times_character_appears(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char(char_count):
    def get_count(item):
        return item[1]
    
    char_list = list(char_count.items())
    char_list.sort(key = get_count, reverse=True)
    return char_list