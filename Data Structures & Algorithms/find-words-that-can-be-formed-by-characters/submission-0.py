class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good = 0
        
        for word in words:
            isValid = True
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    isValid = False
                    break

            if isValid:
                good += len(word)

        return good