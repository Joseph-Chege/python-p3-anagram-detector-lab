# your code goes here!

class Anagram:
    def __init__(self, word=None):
        self._word = None
        if word is not None:
            self.word = word

    def match(self, list):
        sorted_word = sorted(self.word)
        return [word for word in list if sorted(word) == sorted_word]
               
    
       
           






        


