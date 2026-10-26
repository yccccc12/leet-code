from typing import List

class Solution(object):
    def majorityElement(self, nums:List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = list(set(nums))

        counts = {n:nums.count(n) for n in unique}

        return max(counts, key=counts.get)


if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,3]
    output = solution.majorityElement(nums)

    print(output)