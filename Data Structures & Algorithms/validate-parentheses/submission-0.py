class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        valid = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in valid:
                if len(stack)>0 and stack[-1] == valid[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False      