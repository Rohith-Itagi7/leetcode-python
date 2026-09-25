class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # li=[]
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             count+=1
        #     li.append(count)
        # return li

        n=len(nums)
        ans=n*[0]
        arr=[(nums[i],i) for i in range(n)]

        def merge_sort(left,right):
            if left>=right:
                return
            mid=(left+right)//2

            merge_sort(left,mid)
            merge_sort(mid+1,right)

            i=left
            j=mid+1
            temp=[]
            right_count=0

            while i<=mid and j<=right:
                if arr[j][0]<arr[i][0]:
                    temp.append(arr[j])
                    right_count+=1
                    j+=1
                else:
                    ans[arr[i][1]] += right_count
                    temp.append(arr[i])
                    i+=1
            while i<=mid:
                ans[arr[i][1]] += right_count
                temp.append(arr[i])
                i+=1
            while j<=right:
                temp.append(arr[j])
                j+=1

            arr[left:right+1]=temp
        merge_sort(0, n - 1)
        return ans



        
                


    
