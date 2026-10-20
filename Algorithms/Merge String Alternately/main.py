class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        n, m = len(word1), len(word2)
        merged = ""

        while i < n or j < m:
            if i < n:
                merged += word1[i]
                i += 1

            if j < m:
                merged += word2[j]
                j += 1

        return merged


if __name__ == "__main__":
    solution = Solution()
    word1 = "ab"
    word2 = "pqrs"

    output = solution.mergeAlternately(word1, word2)

    print(output)
