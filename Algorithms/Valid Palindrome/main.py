class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        str_s = "".join([c.lower() for c in s if c.isalnum()])
        
        return str_s == str_s[::-1]

    
if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    output = solution.isPalindrome(s)

    print(output)