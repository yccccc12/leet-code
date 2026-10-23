from typing import List

class Solution(object):
    def findClosestNumber(self, nums : List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min([abs(num) for num in nums])

        closest_num = max([num for num in nums if abs(num) == min_num])

        return closest_num

    def findClosestNumber2(self, nums : List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest_num = nums[0]

        for num in nums:
            if abs(num) < abs(closest_num):
                closest_num = num

        if abs(closest_num) in nums:
            return abs(closest_num)

        return closest_num



    
if __name__ == "__main__":
    solution = Solution()
    nums = [-50000, -50000]
    output = solution.findClosestNumber2(nums)

    print(output)