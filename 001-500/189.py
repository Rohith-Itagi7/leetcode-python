class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%(len(nums))
        nums[:]=nums[-k:] + nums[:-k]
         
    # def rotate(self, nums, k):
    #     n = len(nums)
    #     k = k % n

    #     for _ in range(k):
    #         last = nums.pop()
    #         nums.insert(0, last)

    # def rotate(self, nums, k):
    #     n = len(nums)
    #     k = k % n

    #     result = [0] * n

    #     for i in range(n):
    #         result[(i + k) % n] = nums[i]

    #     nums[:] = result

    # class Solution:
    # def rotate(self, nums, k):
    #     n = len(nums)
    #     k = k % n

    #     def reverse(left, right):
    #         while left < right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

    #     reverse(0, n - 1)
    #     reverse(0, k - 1)
    #     reverse(k, n - 1)
