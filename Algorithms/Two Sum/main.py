from typing import List

class Solution(object):
    def twoSum(self, nums:List[int], target:int)-> List[int]:
        if len(nums) == 2:
            return [0, 1]

        for num in nums:
            y = target - num

            if nums.count(y) == 1 and nums.index(num) != nums.index(y):
                return [nums.index(num), nums.index(y)]
            elif nums.count(y) > 1 and nums.index(num) == nums.index(y):
                return [nums.index(num), nums.index(y, nums.index(y) + 1)]

    def twoSum2(self, nums:List[int], target:int)-> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            y = target - num

            if y in seen:
                return [seen[y], i]

            seen[num] = i

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 4, 3]
    output = solution.twoSum2(nums, 6)

    print(output)
