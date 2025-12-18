from stats import get_num_words,get_num_character,get_sorted_characters
import sys 

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_test(book_path)

    word_count = get_num_words(text)
    char_counts = get_num_character(text)
    sorted_chars = get_sorted_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()