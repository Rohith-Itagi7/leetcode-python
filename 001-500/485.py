class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_count=0
        for num in nums:
            if num==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
        return max_count
        # count = max_count = 0
        # for num in nums:
        #     count=count+1 if nums == 1 else 0
        #     max_count=max(max_count,count)
        
        # return max_count
