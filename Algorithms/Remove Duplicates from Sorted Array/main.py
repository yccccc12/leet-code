from typing import List

class Solution(object):
    def removeDuplicates(self, nums:List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        unique = sorted(list(set(nums)))
        i = 0
        j = 1

        while unique != nums[:len(unique)] and j < len(nums):
            if nums[i] == nums[j]:

                nums.pop(i)
                nums.append(1000)

            else:
                i += 1
                j += 1

        return len(unique)

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,0,0,0,3,3]
    output = solution.removeDuplicates(nums)

    print(output)

