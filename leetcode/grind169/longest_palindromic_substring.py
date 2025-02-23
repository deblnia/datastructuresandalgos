def longestPalindrome(s: str) -> str:
    # brute force is to generate all substrings and check if palindromes
    # substrings = []
    # for i in range(len(s)):
    #     for j in range(i, len(s)):
    # remember that this is i through j inclusive
    #         substrings.append(s[i : j + 1])
    # palindromes = [x for x in substrings if x == x[::-1]]
    # return max(palindromes, key=len)

    def expand(s, left, right):
        # expands outwards as long as the characters are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    max_palindrome = ""
    for i in range(len(s)):
        # length is odd
        palindrome = expand(s, i, i)
        if len(palindrome) > len(max_palindrome):
            max_palindrome = palindrome
        # length is even, need to pick the middle character
        palindrome = expand(s, i, i + 1)
        if len(palindrome) > len(max_palindrome):
            max_palindrome = palindrome
    return max_palindrome


assert longestPalindrome("babad") == "bab"
assert longestPalindrome("cbbd") == "bb"
