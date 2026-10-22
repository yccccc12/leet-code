class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

        return s 


if __name__ == "__main__":
    solution = Solution()
    s = ["h","e","l","l","o"]
    output = solution.reverseString(s)

    print(output)
