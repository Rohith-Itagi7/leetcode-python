class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
               count+=1
        return count<=1
        
        # # drops counts how many times the sequence "falls" (a descent occurs)
        # drops = 0

        # # Traverse consecutive pairs to count descents in the linear portion
        # for i in range(1, len(nums)):

        #     # If previous element is greater than current, it's a drop
        #     if nums[i - 1] > nums[i]:
        #         drops += 1  # Increment drop counter

        # # Check the wrap-around: last element compared to first (circular check)
        # if nums[-1] > nums[0]:
        #     drops += 1  # Wrap-around drop found → another descent at rotation boundary

        # # A valid rotated sorted array has at most 1 drop (the rotation point)
        # # 0 drops → already sorted, 1 drop → exactly one rotation, 2+ → invalid
        # return drops < 2
