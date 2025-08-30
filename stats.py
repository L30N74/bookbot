import string
import unicodedata

def base_letter_or_none(char: str) -> str | None:
    # decompose accents
    decomposed = unicodedata.normalize('NFKD', char)
    out: list[str] = []
    for ch in decomposed:
        # skip combining marks
        if unicodedata.category(ch) == 'Mn':
            continue
        out.append(ch)
    # join, lowercase, and keep only ascii letters
    s = ''.join(out).lower()
    return s if len(s) == 1 and s in string.ascii_lowercase else None


def get_num_words(string: str) -> int:
    words = string.split()
    return len(words)


def get_character_count(text: str) -> dict[str, int]:
    # seen: set[str] = set()
    characters: dict[str, int] = {}
    for char in text:
        char = char.lower()
        if not char.isalpha():
            continue
        # char = base_letter_or_none(char)
        # if char is None:
        #     continue
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    return characters


def get_sorted_list(characters: dict[str, int]) -> list[dict[str, int]]:
    sorted_list = []
    for key in characters:
        di = {
            "char": key,
            "num": characters[key]
        }
        sorted_list.append(di)
    return sorted(sorted_list, key=lambda x: x["char"])
