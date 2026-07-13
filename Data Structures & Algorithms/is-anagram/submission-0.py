class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif len(s) == len(t) and sorted(s) == sorted(t):
            return True
        elif len(s) != len(t) or sorted(s) != sorted(t):
            return False