def isPalindrome(s: str) -> bool:
    s = s.lower().strip()
    s = ''.join([x for x in s if x.isalnum()])
    return s == s[::-1]

assert isPalindrome("A man, a plan, a canal: Panama")
assert not isPalindrome("race a car")
assert isPalindrome(" ")
