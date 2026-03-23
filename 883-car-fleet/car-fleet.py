class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for pos,sp in pairs:
            atime = ((target-pos)/sp)
            if not stack or atime > stack[-1]:
                stack.append(atime)
        return len(stack)