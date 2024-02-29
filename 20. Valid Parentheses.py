# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Example 1:=====================
# Input: s = "()[]{}"
# Output: true

# Example 2:=====================
# Input: s = "(]"
# Output: false

from typing import List
class Solution:
    def check_parentheses(self, s:List):
        parentheses = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        blank_list = []
        for i in s:
            if i in parentheses:
                blank_list.append(i)
            elif len(blank_list) == 0 or parentheses[blank_list.pop()] != i:
                return False
        return len(blank_list) == 0

s = "()[]{}"            
ValidParentheses = Solution()
print(ValidParentheses.check_parentheses(s))
