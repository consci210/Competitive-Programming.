class TrieNode : 
    def __init__(self, val=0 ) :
        self.value = val 
        self.children = {}
        self.is_terminal = False 

class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        current = self.root 
        for letter in word :
            if letter not in current.children :
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]
        current.is_terminal = True 

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word :
            if letter not in current.children:
                return False 
            current = current.children[letter]
        return current.is_terminal 

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix :
            if letter not in current.children :
                return False 
            current = current.children[letter]
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)