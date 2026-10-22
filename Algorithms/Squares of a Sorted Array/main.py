from typing import List

class Solution(object):
    def sortedSquares(self, nums : List[int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = [num ** 2 for num in nums]
        return sorted(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [-4, -1, 0, 3, 10]
    output = solution.sortedSquares(nums)

    print(output)