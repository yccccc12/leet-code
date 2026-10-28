from typing import List

class Solution(object):
    def search(self, nums:List[int], target:int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid_pos = (low + high) // 2

            if target == nums[mid_pos]:
                return mid_pos

            if target > nums[mid_pos]:
                low = mid_pos + 1

            if target < nums[mid_pos]:
                high = mid_pos - 1

        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    output = solution.search(nums, target)

    print(output)