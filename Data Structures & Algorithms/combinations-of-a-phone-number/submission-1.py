class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        output = []
        if len(digits) == 0:
            return []

        elif len(digits) == 1:
            return (list(numMap[digits[0]]))
        
        elif len(digits) == 2:
            group1 = numMap[digits[0]]
            group2 = numMap[digits[1]]

            for i in group1:
                for j in group2:
                    output.append(i+j)

        elif len(digits) == 3:
            group1 = numMap[digits[0]]
            group2 = numMap[digits[1]]
            group3 = numMap[digits[2]]


            for i in group1:
                for j in group2:
                    for k in group3:
                        output.append(i+j+k)
                
        elif len(digits) == 4:
            group1 = numMap[digits[0]]
            group2 = numMap[digits[1]]
            group3 = numMap[digits[2]]
            group4 = numMap[digits[3]]

            for i in group1:
                for j in group2:
                    for k in group3:
                        for l in group4:
                            output.append(i+j+k+l)
        
        return output
               

        
