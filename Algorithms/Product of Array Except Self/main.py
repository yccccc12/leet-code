from typing import List

class Solution(object):
    def productExceptSelf(self, nums : List[int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # This solution will cause Time Limit Exceeded Error
        product_nums = []

        for i in range(len(nums)):
            nums_i = nums[:]
            nums_i.remove(nums[i])

            product = 1

            for num in nums_i:
                product *= num

            product_nums.append(product)

        return product_nums

    def productExceptSelf2(self, nums : List[int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        product_nums = [1] * n
        prefix, suffix = 1, 1

        for i in range(n):
            product_nums[i] = prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            product_nums[i] *= suffix
            suffix *= nums[i]
            
        return product_nums

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 4, 5, 6]
    output = solution.productExceptSelf2(nums)

    print(output)