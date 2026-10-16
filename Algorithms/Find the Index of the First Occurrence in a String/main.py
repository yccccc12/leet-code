class Solution(object):
    def strStr(self, haystack:str, needle:str):
        """
        :type haystack: str
        :type needle: str
        :rtype int
        """

        if len(haystack) < len(needle):
            return -1

        return haystack.find(needle)

    def strStr2(self, haystack:str, needle:str):
        """
        :type haystack: str
        :type needle: str
        :rtype int
        """

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1



if __name__ == "__main__":
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    output = solution.strStr2(haystack, needle)

    print(output)