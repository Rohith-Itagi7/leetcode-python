class Solution(object):
    def summaryRanges(self, nums):
        result = []

        if not nums:
            return result

        start = 0

        for i in range(1, len(nums)):
            # If numbers are NOT consecutive
            if nums[i] != nums[i - 1] + 1:

                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start]) + "->" + str(nums[i - 1]))

                start = i

        # Add the final range
        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            result.append(str(nums[start]) + "->" + str(nums[-1]))

        return result
