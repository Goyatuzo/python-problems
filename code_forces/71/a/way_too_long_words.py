
def way_too_long_words(word: str) -> str:
    """
    Let's consider a word too long, if its length is strictly more than 10 characters.
    All too long words should be replaced with a special abbreviation.

    This abbreviation is made like this: we write down the first and the last letter
    of a word and between them we write the number of letters between the first and
    the last letters. That number is in decimal system and doesn't contain any leading
    zeroes.
    """
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]

    return word

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(way_too_long_words(input()))