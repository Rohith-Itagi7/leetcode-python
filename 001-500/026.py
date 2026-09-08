class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
               i+=1
               nums[i]=nums[j]
        return i+1
        
    #     if not nums:
    #         return 0
    #     res = 1
    #     for i in range(1, len(nums)):
    #         if nums[i] != nums[i - 1]:
    #             nums[res] = nums[i]
    #             res += 1
    #     return res

        # res = 0

        # for i in range(len(nums) - 1):
        #     if nums[i] != nums[i + 1]:
        #         nums[res] = nums[i]
        #         res += 1

        # nums[res] = nums[-1]
        # res += 1















    
