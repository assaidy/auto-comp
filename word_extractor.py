import string
from collections import defaultdict


def clean_word(word: str, remove_digits: bool = False) -> str:
    to_remove: str = string.punctuation + string.whitespace
    if remove_digits:
        to_remove += string.digits
    return word.strip(to_remove).lower()


async def read_entire_file_words(file_path: str) -> dict[str, int]:
    """
    return all unique words in a file with its frequency count
    """

    words_to_count: dict[str, int] = defaultdict(int)
    punctuation_and_spaces = set(string.punctuation + string.whitespace)
    with open(file_path, "r") as file:
        word = ""
        while ch := file.read(1):
            if ch in punctuation_and_spaces:
                if word:
                    words_to_count[clean_word(word)] += 1
                    word = ""
                continue
            word += ch
    return words_to_count
