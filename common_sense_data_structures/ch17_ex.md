
```python 
class TrieNode: 
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def insert(self, word):
        current_node = self.root 
        for char in word: 
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else: 
                new_node = TrieNode()
                current_node.children[char] = new_node 
                current_node = new_node 
        current_node.children["*"] = None 
    
    # building autocomplete now 
    
    def collect_all_words(self, words, node=None, word=""):
        current_node = node or self.root 
        for key, child_node in current_node.children.items():
            if key == "*"
                words.append(word)
            else: 
                self.collect_all_words(words, child_node, word + key) 
        return words 

    def autocomplete(self, prefix): 
        current_node = self.search(prefix)

        if not current_node: 
            return None 

        return self.collect_all_words([], current_node)

```

## Question 1 


