class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        if len(digits) == 0:
            return []

        numMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
                }

        
        res = []

        def backtrack(currString, i):
            if len(currString) == len(digits):
                res.append(currString)
                return
            
            
            for char in numMap[digits[i]]:
                currString += char
                backtrack(currString, i+1)
                currString = currString[:-1]            


        backtrack("", 0)

        return res

        
