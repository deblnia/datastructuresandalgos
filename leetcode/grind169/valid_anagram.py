from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    # return sorted(s) == sorted(t)
    return Counter(s) == Counter(t)


assert isAnagram(s="anagram", t="nagaram")
assert not isAnagram(s="rat", t="car")
