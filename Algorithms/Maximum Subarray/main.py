from typing import List

class Solution(object):
    def maxSubArray(self, nums:List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]

        for i in range(1, len(nums)):
            dp.append(max(nums[i] + dp[i-1], nums[i]))

        return max(dp)
        

if __name__ == "__main__":
    solution = Solution()
    nums = [5,4,-1,7,8]
    output = solution.maxSubArray(nums)

    print(output)