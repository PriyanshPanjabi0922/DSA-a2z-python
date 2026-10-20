# Leetcode version of my solution:

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        
        low = 0
        high  = len(nums) - 1
        n = len(nums)

        def merge(nums,low,mid,high):

            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high :
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1

            while left <=mid:
                temp.append(nums[left])
                left+=1

            while right <= high:
                temp.append(nums[right])
                right+=1

            for i in range(low,high+1):
                nums[i] = temp[i - low]

        def solution(nums,low,high):

            if low >= high:
                return 0
            
            mid = (low +high )//2
            count = 0
            left_count = solution(nums, low, mid)
            right_count = solution(nums, mid + 1, high)
            j = mid + 1
            for i in range(low,mid+1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j+=1  
                count += j - (mid+1) 

            merge(nums, low, mid, high)

            return left_count + right_count + count
        return solution(nums,0,n-1)

        