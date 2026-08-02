class Solution:
    def isPalindrome(self, s: str) -> bool:
        for letter in s:
            if not letter.isalnum():
                s = s.replace(letter,"")
        s = s.lower()
        return s[::-1] == s
        