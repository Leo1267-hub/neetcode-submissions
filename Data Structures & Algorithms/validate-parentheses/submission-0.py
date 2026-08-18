class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        have = {']':'[',
                ')':'(',
                '}':'{'
        }
        for b in s:
            if b in ']})':
                if stack and stack[-1] == have[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return len(stack) == 0