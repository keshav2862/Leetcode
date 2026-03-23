class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)
        stack = []
        for pos,sp in pairs:
            atime = ((target-pos)/sp)
            if not stack or atime > stack[-1]:
                stack.append(atime)
        return len(stack)