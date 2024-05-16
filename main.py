#!/usr/bin/env python3

from trie import Trie
from word_extractor import read_entire_file_words


def main() -> None:
    PATH = "./t8.shakespeare.txt"

    trie = Trie()

    print("[INFO] processing words...", end="", flush=True)
    words_with_count = read_entire_file_words(PATH)
    trie.fill(list(words_with_count.keys()))

    try:
        while True:
            key = input("\nfind somthing: ").strip().lower()
            print("-" * 20)
            completion_list = trie.complete(key)
            if not completion_list:
                print("[INFO] no results found.")
                continue
            for word in completion_list:
                print(">", word)
    except KeyboardInterrupt:
        exit(1)


if __name__ == "__main__":
    main()
