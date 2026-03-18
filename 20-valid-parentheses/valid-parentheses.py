class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0