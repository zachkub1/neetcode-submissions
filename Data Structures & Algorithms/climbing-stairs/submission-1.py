class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev = 1
        curr = 2
        total = 0

        for i in range(3,n+1):
            total = curr + prev
            prev = curr
            curr = total
        return total