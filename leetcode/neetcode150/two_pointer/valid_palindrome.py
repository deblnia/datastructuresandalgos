

def isPalindrome(s:str)->bool:
    # case insensitive and remove non-alphanumeric characters
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    # two pointers, one from start of arry and one from end
    # if they are not equal, can't be a palindrome
    l, r = 0 , len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


assert isPalindrome("Was it a car or a cat I saw?")
assert not isPalindrome("tab a cat")
