class Solution(object):
    def isPalindrome(self, x:int)->bool:
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        n = len(x)

        while i < n // 2:
            if x[0] != x[-1]:
                return False
            else:
                x = x[1:-1]
                i += 1
    
        return True

    def isPalindrome2(self, x:int)->bool:
        return str(x) == str(x)[::-1] # [start:end:step size]. if sign of step size is negative, it means move backward at the end

if __name__ == "__main__":
    solution = Solution()
    x = 123321
    print(solution.isPalindrome2(x))