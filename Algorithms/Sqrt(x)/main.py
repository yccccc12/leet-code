class Solution(object):
    def mySqrt(self, x: int):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            elif mid * mid > x:
                right = mid - 1

        return right

        

if __name__ == "__main__":
    solution = Solution()
    x = 8
    # x = 2147395599
    output = solution.mySqrt(x)

    print(output)