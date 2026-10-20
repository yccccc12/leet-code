from typing import List

class Solution(object):
    def twoSum(self, numbers:List[int], target:int):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Own solution, but having Time Limit Exceeded Error at Leetcode's platform
        for i, num in enumerate(numbers):
            y = target - num

            if num == y:
                return [i+1, numbers.index(y, i+1)+1]

            if y in numbers:
                return [i+1, numbers.index(y) + 1]

    def twoSum2(self, numbers:List[int], target:int):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Two pointers solution
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]

            elif total < target:
                left += 1

            else:
                right -= 1
    
            

if __name__ == "__main__":
    solution = Solution()
    numbers = [5,25,75]
    target = 100

    output = solution.twoSum(numbers, target)

    print(output)