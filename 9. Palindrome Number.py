# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:==================
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:==================
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Sulotion:
    def palindrome(self, x):
        if x < 0:
            return False
        
        temp = x
        reverse_x = 0
        while temp != 0:
            last_num_x = temp%10
            reverse_x = reverse_x*10+ last_num_x
            temp//=10
        return x == reverse_x

is_palindrome = Sulotion()
print(is_palindrome.palindrome(56896))
print(is_palindrome.palindrome(65656))
print(is_palindrome.palindrome(-65656))
            
