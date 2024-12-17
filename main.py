

def main():
        with open("books/frankenstein.txt") as f:
                file_contents = f.read()
        report(file_contents)

def word_count(book_text):
        return len(book_text.split())

def character_counts(book_text: str):
        char_counts_dict = {
                (1, "a"): book_text.lower().count("a"),
                (2, "b"): book_text.lower().count("b"),
                (3, "c"): book_text.lower().count("c"),
                (4, "d"): book_text.lower().count("d"),
                (5, "e"): book_text.lower().count("e"),
                (6, "f"): book_text.lower().count("f"),
                (7, "g"): book_text.lower().count("g"),
                (8, "h"): book_text.lower().count("h"),
                (9, "i"): book_text.lower().count("i"),
                (10, "j"): book_text.lower().count("j"),
                (11, "k"): book_text.lower().count("k"),
                (12, "l"): book_text.lower().count("l"),
                (13, "m"): book_text.lower().count("m"),
                (14, "n"): book_text.lower().count("n"),
                (15, "o"): book_text.lower().count("o"),
                (16, "p"): book_text.lower().count("p"),
                (17, "q"): book_text.lower().count("q"),
                (18, "r"): book_text.lower().count("r"),
                (19, "s"): book_text.lower().count("s"),
                (20, "t"): book_text.lower().count("t"),
                (21, "u"): book_text.lower().count("u"),
                (22, "v"): book_text.lower().count("v"),
                (23, "w"): book_text.lower().count("w"),
                (24, "x"): book_text.lower().count("x"),
                (25, "y"): book_text.lower().count("y"),
                (26, "z"): book_text.lower().count("z"),
                (27, "."): book_text.lower().count("."),
                (28, "!"): book_text.lower().count("!"),
                (29, ","): book_text.lower().count(","),
                (30, ";"): book_text.lower().count(";"),
                (31, ":"): book_text.lower().count(":"),
                (32, "\'"): book_text.lower().count("\'"),
                (33, "\""): book_text.lower().count("\""),
                (34, "\\"): book_text.lower().count("\\"),
                (35, "/"): book_text.lower().count("/"),
                (36, "?"): book_text.lower().count("?"),
                (37, "("): book_text.lower().count("("),
                (38, ")"): book_text.lower().count(")"),
        }
        return char_counts_dict

def report(book_text):
        sorted_character_counts = sorted(character_counts(book_text).items(), key=lambda item: item[0])
        print("---Begin Report of books/frankenstein.txt---")
        print(f"Frankenstein has {word_count(book_text)} words" )

        for item in sorted_character_counts:
                item_char_key = item[0]
                print(f"{item_char_key[1]} occurs {item[1]} times")
        print(" ---End Report---")

main()