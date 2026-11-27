class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(", "}":"{", "]":"["}
        stack = []
        for letter in s:
            if letter not in valid:
                stack.append(letter)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if valid[letter] != bracket:
                    return False
        
        if stack:
            return False
        return True