class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        def gcd(a, b):
            if a < 0: a = -a
            if b < 0: b = -b
            while b:
                a, b = b, a % b
            return a

        def slopeval(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            dy = y2 - y1
            dx = x2 - x1

            if dx == 0 and dy == 0:
                return None
            if dx == 0:
                return (1, 0)
            if dy == 0:
                return (0, 1)

            g = gcd(dy, dx)
            dy //= g
            dx //= g

            if dx < 0:
                dx = -dx
                dy = -dy

            return (dy, dx)

        ans = 1
        for i in range(len(points)):
            slopes = {}
            dup = 0
            best = 0
            for j in range(i+1, len(points)):
                s = slopeval(points[i], points[j])
                if s is None:
                    dup += 1
                    continue
                slopes[s] = slopes.get(s, 0) + 1
                if slopes[s] > best:
                    best = slopes[s]
            if best + dup + 1 > ans:
                ans = best + dup + 1

        return ans