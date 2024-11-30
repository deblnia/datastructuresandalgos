'''
Brute force way 
''' 

class Solution:
  def checkIfPangram(self, sentence):
    return set(sentence) == set('abcdefghijklmnopqrstuvwxyz')

'''
Using built in functions 
''' 
class Solution:
    def checkIfPangram(self, sentence): 
        seen = set()
        for i in range(len(sentence)): 
            curr = sentence[i].lower()
            if curr.isalpha():
                seen.add(curr) 
        return len(seen) == 26
