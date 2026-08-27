class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0]*n
        for i in nums:
            if temp[i] != 0:
                return i
            else:
                temp[i]=1