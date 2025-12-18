from stats import get_num_words,get_num_character

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 
       
def main():
    str = get_book_test("./books/frankenstein.txt")
    num_words = get_num_words(str)
    print(f"Found {num_words} total words")
    print(get_num_character(str))

main()