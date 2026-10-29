class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occur = set()
        n = str(n)

        if len(n) == 1 and n == "1":
            return True
        
        while len(n) >= 1 and n not in occur:
            occur.add(n)

            x = 0
            for c in n:
                x += int(c) ** 2

            if x == 1:
                return True

            n = str(x)

        return False


if __name__ == "__main__":
    solution = Solution()
    n = 7
    output = solution.isHappy(n)

    print(output)