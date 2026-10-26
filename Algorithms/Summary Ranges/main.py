from typing import List

class Solution(object):
    def summaryRanges(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            while i + 1 < n and nums[i] + 1 == nums[i+1]:
                i += 1

            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans
                 
if __name__ == "__main__":
    solution = Solution()
    nums = [0,2,3,4,6,8,9]
    output = solution.summaryRanges(nums)

    print(output)