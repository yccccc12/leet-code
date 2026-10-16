from typing import List

class Solution(object):
    def searchInsert(self, nums: List[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        filter_nums = [i for i in nums if i < target]
        return len(filter_nums)

    def searchInsert2(self, nums: List[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Complexity O(log n)
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

        return low



if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    output = solution.searchInsert2(nums, target)

    print(output)