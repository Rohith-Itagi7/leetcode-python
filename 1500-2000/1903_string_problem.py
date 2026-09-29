def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):  
          if int(num[i])%2 !=0: 
            return num[ :i+1]
        return ''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        for i in range(len(num) - 1, -1, -1) :
            if num[i] in {'1','3','5','7','9'} :
                return num[:i+1]
        return ''

# Specific pattern:

# Right-to-left search → first valid digit → return prefix → stop.

# This is a greedy right-to-left scanning pattern.
# 2. How do I recognize this pattern?

# Look for:

# "largest odd number"
# "substring"
# "prefix"
# "rightmost"
# A condition that depends on the last digit
# Once the correct position is found, everything before it is automatically part of the answer

# The strongest clue here is:

# Odd number → last digit must be odd.

# Then:

# Largest → choose the rightmost possible odd ending.
