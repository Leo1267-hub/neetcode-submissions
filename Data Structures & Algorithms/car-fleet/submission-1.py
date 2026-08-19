class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs.sort()
        pairs = pairs[::-1]
        stack = []
        fleets = len(pairs)
        for i in range(len(pairs)):
            p,s = pairs[i]
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)