from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs: List[str])->str:
        """
        :type strs: List[str]
        :rtype: str
        """
        
        n = min(len(s) for s in strs)

        unique_str = ""
        for i in range(n+1):
            match = set([s[:i] for s in strs])

            if len(match) == 1:
                unique_str = strs[0][:i]
           
        return unique_str

if __name__ == "__main__":
    solution = Solution()
    strs = ["dog","racecar","car"]
    output = solution.longestCommonPrefix(strs)

    print(output)