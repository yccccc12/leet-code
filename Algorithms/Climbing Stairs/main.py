class Solution(object):
    def climbStairs(self, n : int):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dp(n):
            if n <= 2:
                return n

            if n in memo:
                return memo[n]
            
            memo[n] = dp(n-1) + dp(n-2)

            return memo[n]

        return dp(n)

if __name__ == "__main__":
    solution = Solution()
    n = 38
    output = solution.climbStairs(n)
    
    print(output)
    