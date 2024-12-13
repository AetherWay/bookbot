import __main__
import pprint

def main():
        with open("books/frankenstein.txt") as f:
                file_contents = f.read()
        print(f"Frankenstein has {word_count(file_contents)} words")
        print("Frankenstein character counts:")
        pprint.pprint(character_counts(file_contents))

def word_count(book_text):
        return len(book_text.split())

def character_counts(book_text: str):
        return {
                "a": book_text.lower().count("a"),
                "b": book_text.lower().count("b"),
                "c": book_text.lower().count("c"),
                "d": book_text.lower().count("d"),
                "e": book_text.lower().count("e"),
                "f": book_text.lower().count("f"),
                "g": book_text.lower().count("g"),
                "h": book_text.lower().count("h"),
                "i": book_text.lower().count("i"),
                "j": book_text.lower().count("j"),
                "k": book_text.lower().count("k"),
                "l": book_text.lower().count("l"),
                "m": book_text.lower().count("m"),
                "n": book_text.lower().count("n"),
                "o": book_text.lower().count("o"),
                "p": book_text.lower().count("p"),
                "q": book_text.lower().count("q"),
                "r": book_text.lower().count("r"),
                "s": book_text.lower().count("s"),
                "t": book_text.lower().count("t"),
                "u": book_text.lower().count("u"),
                "v": book_text.lower().count("v"),
                "w": book_text.lower().count("w"),
                "x": book_text.lower().count("x"),
                "y": book_text.lower().count("y"),
                "z": book_text.lower().count("z"),
                ".": book_text.lower().count("."),
                "!": book_text.lower().count("!"),
                ",": book_text.lower().count(","),
                ";": book_text.lower().count(";"),
                ":": book_text.lower().count(":"),
                "\'": book_text.lower().count("\'"),
                "\"": book_text.lower().count("\""),
                "\\": book_text.lower().count("\\"),
                "/": book_text.lower().count("/"),
                "?": book_text.lower().count("?"),
                "(": book_text.lower().count("("),
                ")": book_text.lower().count(")"),
        }

main()