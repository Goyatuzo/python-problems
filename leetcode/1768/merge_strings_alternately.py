def merge_strings_alternately(word1: str, word2: str) -> str:
    i = 0
    len1 = len(word1)
    len2 = len(word2)

    joined = ''

    while i < min(len1, len2):
        joined += word1[i] + word2[i]
        i += 1

    if i < len1:
        joined += word1[i:]
    else:
        joined += word2[i:]

    return joined
