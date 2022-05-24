# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        
        if nums[end] == target:
            return end
        elif nums[end] < target:
            return end+1
        elif nums[start] == target or nums[start]>target:
            return start
        
        while (start+1<end):
            mid=int((start+end)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end=mid
            else:
                start=mid
        return end
        
