class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        for i, ch in enumerate(s):

            if ch == ']' or ch == ')' or ch == '}':
                if stack and stack[-1] == ch:
                    stack.pop()
                else:
                    return False
            elif ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
        return not stack
