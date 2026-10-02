class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()

        left = 0
        window_sum = 0
        answer = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            # Cost to make every element in the window equal to nums[right]
            cost = nums[right] * (right - left + 1) - window_sum

            # If cost is too high, shrink the window
            while cost > k:
                window_sum -= nums[left]
                left += 1

                cost = nums[right] * (right - left + 1) - window_sum

            answer = max(answer, right - left + 1)

        return answer
