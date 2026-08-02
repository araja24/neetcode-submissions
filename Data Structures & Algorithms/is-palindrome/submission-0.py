class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        for letter in s:
            if not letter.isalnum():
                s = s.replace(letter,"")

        return s[::-1] == s
        