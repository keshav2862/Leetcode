class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while ans and a < 0 < ans[-1]:
                if -a > ans[-1]:
                    ans.pop()
                    continue
                elif -a == ans[-1]:
                    ans.pop()
                break
            else:
                ans.append(a)

        return ans