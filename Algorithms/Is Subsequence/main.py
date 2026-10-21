class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        overlap = []
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                overlap.append(s[i])
                i += 1
                j += 1
                
            else:
                j += 1

        if len(overlap) == len(s):
            return True

        return False


            

if __name__ == "__main__":
    solution = Solution()
    s = ""
    t = "ahbgdc"

    output = solution.isSubsequence(s, t)

    print(output)