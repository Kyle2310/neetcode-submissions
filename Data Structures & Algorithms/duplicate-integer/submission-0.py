class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sort_array = sorted(nums)
        for i in range(0,len(nums)-1):
            if sort_array[i] == sort_array[i+1]:
                    return True
        return False