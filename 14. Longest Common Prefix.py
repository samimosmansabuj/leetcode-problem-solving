# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:==============================
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:==============================
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
class Solution:
    def CommonPrefix(self, strs:List):
        prefix = ""
        strs_zip = list(zip(*strs))
        for i in strs_zip:
            if len(set(i)) == 1:
                prefix+=i[0]
            else:
                break
        return prefix

strs1 = ["flowerfl","f5lowfl","6lightfl"]
strs2 = ["flower","flow","flight"]

StrPrefix = Solution()
print(StrPrefix.CommonPrefix(strs1))
print(StrPrefix.CommonPrefix(strs2))

