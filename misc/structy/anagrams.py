from collections import Counter
def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)


assert anagrams('cats', 'tocs') == False 
assert anagrams('restful', 'fluster') == True