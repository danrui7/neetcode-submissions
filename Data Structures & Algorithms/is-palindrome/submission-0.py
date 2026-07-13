class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for c in s.lower():
            if c.isalnum():
                s1 += c
        s2 = "".join(reversed(s1))
        if s1 == s2:
            return True
        else:
            return False

        
        