# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Example 1:================
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:================
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        
        return ans

s = "MCMXCIV"
is_roman_number = Solution()
print(is_roman_number.romanToInt(s))

