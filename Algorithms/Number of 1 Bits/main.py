class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        bin_str = ""

        while n != 0:
            remainder = n % 2
            n //= 2
            bin_str += str(remainder)

        return bin_str.count('1')
    
if __name__ == "__main__":
    solution = Solution()
    n = 128
    output = solution.hammingWeight(n)

    print(output)