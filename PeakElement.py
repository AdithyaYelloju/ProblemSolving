A peak element 
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


# Time O(n)
def solve_brut(nums):

    if(nums[0]>nums[1]):
        return nums[0]
   
    if(nums[-1] > nums[-2]):
        return nums[-1]
   
    for i in range(1,len(nums)-1):
        if(nums[i]> nums[i-1] and nums[i] > nums[i+1]):
            return nums[i]

# Time O(nlogn)
def solve(nums):
    start = 0
    end = len(nums)

    while(start < end):
        mid = (start+end)//2

        if(nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
            return nums[mid]

        if(nums[mid+1] > nums[mid]):
            start = mid+1

        elif(nums[mid+1] < nums[mid]):
            end  = mid

        print(nums[mid], start, end)




nums = [1,2,1,3,5,6,4]
print(solve(nums)) #6
