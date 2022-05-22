class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for indx, num in enumerate(nums):
            if num == target:
                return indx
        return -1
