class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                previous_index = seen[nums[i]]

                if i - previous_index <= k:
                    return True

            seen[nums[i]] = i

        return False
        
