class Node:
    def __init__(self, letter: str, value: object = None) -> None:
        if len(letter) != 1:
            raise ValueError("Only single letters are allowed as nodes")
        
        self.letter = letter
        self.children = dict()
        self.value = value


    def isFinal(self) -> bool:
        return False if self.value == None else True


    def insert(self, word: str, value: object = True) -> None:
        if len(word) == 0:
            raise ValueError("Inserting the empty word in non root nodes is not possible")

        v = value if len(word) == 1 else None
        child = self.children.setdefault(word[0], Node(word[0]))
        child.value = v
        if len(word) > 1:
            child.insert(word[1:], value)


    def longestMatch(self, word: str) -> str:
        child = self.children.get(word[0:1])
        childsMatch = ''
        if child != None:
            childsMatch = child.longestMatch(word[1:])
        if childsMatch != '':
            return self.letter + childsMatch
        else:
            return self.letter if self.isFinal() else ''


    def get(self, word: str) -> object:
        child = self.children.get(word[0:1])
        if child is None:
            return self.value if len(word) == 0 else None
        else:
            return child.get(word[1:])

    
    def delete(self, word: str) -> None:
        if len(word) == 0:
            if not self.isFinal():
                raise KeyError
            self.value = None
        else:
            child = self.children.get(word[0])
            if child:
                child.delete(word[1:])
                if len(child.children) == 0 and not child.isFinal():
                    del self.children[word[0]]
            else:
                raise KeyError
        

    def __delitem__(self, key: str) -> None:
        self.delete(key)

        
    def __getitem__(self, key: str) -> object:
        r = self.get(key)
        if r is None:
            raise KeyError
        return r


    def __setitem__(self, key: str, value: object) -> None:
        self.insert(key, value)
        
        
    def __contains__(self, word: str) -> bool:
        return True if self.longestMatch(word) == word else False


    def __repr__(self) -> str:
        return "'{l}': ({v}, {c})".format(l=self.letter,
                                          v=repr(self.value),
                                          c=repr(set(self.children.values())))
            
        
    
class PrefixTree(Node):
    def __init__(self, words: list[str]=[]) -> None:
        self.letter = ''
        self.value = None
        self.children = dict()
        for w in words:
            self.insert(w)


    def insert(self, word: str, value: object = True) -> None:
        if len(word) == 0:
            self.value = value
        else:
            super().insert(word, value)


    def longestMatch(self, word: str) -> str:
        m = super().longestMatch(word)
        if m == '':
            return '' if self.isFinal() else None
        else:
            return m


class SuffixTree(PrefixTree):
    def __init__(self, words: list[str] = []) -> None:
        revwords = [w[::-1] for w in words]
        super().__init__(words)


    def insert(self, word: str, value: object = True) -> None:
        super().insert(word[::-1], value)


    def longestMatch(self, word: str) -> str:
        return super().longestMatch(word[::-1])[::-1]


    def get(self, word: str) -> object:
        return super().get(word[::-1])


    def delete(self, word: str) -> None:
        super().delete(word[::-1])
