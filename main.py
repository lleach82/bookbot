import sys
from stats import num_of_words, num_of_characters, sorted_characters

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    number_words = num_of_words(book)
    number_letters = num_of_characters(book)
    sorted_letters = sorted_characters(number_letters)
    print(f"Found {number_words} total words")
    
    for entry in sorted_letters:
        print(f"{entry['character']}: {entry['count']}")

main()
