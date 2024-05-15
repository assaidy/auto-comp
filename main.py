#!/usr/bin/env pypy3

import asyncio

from trie import Trie
from word_extractor import read_entire_file_words

async def main() -> None:
    PATH = "./t8.shakespeare.txt"
    words_with_count = await read_entire_file_words(PATH)

    trie = Trie()
    await trie.fill(list(words_with_count.keys()))

    key = input("find somthing: ").strip().lower()
    for word in trie.complete(key):
        print(">", word)


if __name__ == "__main__":
    asyncio.run(main())
