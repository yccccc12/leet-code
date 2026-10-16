from typing import List

class Solution(object):
    def plusOne(self, digits: List[int]):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        unique = set(digits)
        if 9 in unique and len(unique) == 1:
            digits = [0 for num in digits if num == 9]
            digits.insert(0, 1)
            return digits
            
        digits[-1] += 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 10:
                return digits

            else:
                digits[i] -= 10
                digits[i-1] += 1

    def plusOne2(self, digits: List[int]):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_num = ''.join(str(i) for i in digits)
        str_num = eval(str_num) + 1

        int_num_list = [int(i) for i in str(str_num)]

        return int_num_list
        

if __name__ == "__main__":
    solution = Solution()
    digits = [8, 9, 9 ,9]
    output = solution.plusOne2(digits)

    print(output)