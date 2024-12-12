import __main__
def main():
        with open("books/frankenstein.txt") as f:
                file_contents = f.read()
                print(f"Frankenstein has {word_count(file_contents)} words")

def word_count(book_text):
        return len(book_text.split())

main()