from stats import *
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        contents = f.read()
        return contents


def print_report(filepath: str, word_count: int, chars: list[dict[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for i in range(0, len(chars)):
        key: str = str(chars[i]["char"])
        value: int = chars[i]["num"]
        print(f"{key}: {value}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    word_count = get_num_words(book_contents)
    chars = get_character_count(book_contents)

    sorted_chars = get_sorted_list(chars)
    print_report(filepath, word_count, sorted_chars)


if __name__ == "__main__":
    main()
