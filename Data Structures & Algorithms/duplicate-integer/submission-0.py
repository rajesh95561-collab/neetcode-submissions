class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set(nums)
        if(len(arr) == len(nums)):
            return False
        return True