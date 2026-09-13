# Trace format
# Step	All important variables/pointers	Values	Condition	Executes	Updated state
# Initial	i, j, result	...	—	—	...
# 1	i, j, result	...	... = True	if	...
# 2	i, j, result	...	... = False	else	...
# 3	i, j, result	...	... = True	if	...

# Then I'll give:

# Simple English
# What happened in Step 1
# What happened in Step 2
# Why the variable changed
# Why the loop stopped
# Complexity
# Time: O(...)
# Space: O(...)

# For your Single Number / XOR problem, if we use:
# the trace will look like:

# Step	Variable	Values	Condition	Executes	Updated state
# Initial	result	0	—	—	result = 0
# 1	num=4	result=0	loop continues	result = result ^ num	result = 4
# 2	num=1	result=4	loop continues	result = result ^ num	result = 5
# 3	num=2	result=5	loop continues	result = result ^ num	result = 7
# 4	num=1	result=7	loop continues	result = result ^ num	result = 6
# 5	num=2	result=6	loop continues	result = result ^ num	result = 4

# Then:

# Loop stops because there are no more elements in nums.

# Final result = 4

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for num in nums:
            result ^= num

        return result
