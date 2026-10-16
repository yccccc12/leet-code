class Solution(object):
    def addBinary(self, a:str, b:str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = int(a, 2) + int(b, 2)
        output = bin(output)[2:]
        return output

    def addBinary2(self, a:str, b:str) -> str:
        bin_a = 0
        bin_b = 0
        for i, c in enumerate(a[::-1]):
            bin_a += pow(2, i) * int(c)

        for i, c in enumerate(b[::-1]):
            bin_b += pow(2, i) * int(c)

        bin_sum = bin_a + bin_b

        bin_sum_str = ""

        while bin_sum > 0:
            bin_sum_str += str(bin_sum % 2)
            bin_sum = bin_sum // 2

        if len(bin_sum_str) == 0:
            return "0"
        
        return bin_sum_str[::-1]



if __name__ == "__main__":
    solution = Solution()

    a = "0"
    b = "0"
    output = solution.addBinary2(a, b)

    print(output)