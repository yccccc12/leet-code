from typing import List

class Solution(object):
    def removeElement(self, nums:List[int], val:int):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
                
        return n

if __name__ == "__main__":
    solution = Solution()

    nums = [0,1,2,2,3,0,4,2]

    val = 2
    output = solution.removeElement(nums, val)

    print(output)
