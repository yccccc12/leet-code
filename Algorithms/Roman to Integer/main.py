class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        special_case = {
            'CM':900,
            'CD':400,
            'XC':90,
            'XL':40,
            'IX': 9,
            'IV': 4,
        }

        num = 0
        for case in special_case.keys():
            if(s.find(case) != -1):
                idx = s.find(case)
                s = s.replace(s[idx:idx+2], "")
                num += special_case[case]
        
 
        for case in dict_roman.keys():
            count = s.count(case, 0, len(s))
            num += dict_roman[case] * count

        
        return num

    def romanToInt2(self, s:str) -> int:
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        count = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n-1 and dict_roman[s[i]] < dict_roman[s[i+1]]:
                count += dict_roman[s[i+1]] - dict_roman[s[i]]
                i += 2
            else:
                count += dict_roman[s[i]]
                i += 1

        return count
                
            
if __name__ == "__main__":
    solution = Solution()
    roman = "III"
    output = solution.romanToInt2(roman)

    print(output)
