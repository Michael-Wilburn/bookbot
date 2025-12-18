def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

       
def main():
    print(get_book_test("./books/frankenstein.txt"))

main()