class Solution(object):
    def numJewelsInStones(self, jewels:str, stones:str):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0

        for c in stones:
            if c in jewels:
                count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    jewels = "abc"
    stones = "aAAbbbbc"
    output = solution.numJewelsInStones(jewels, stones)

    print(output)
    