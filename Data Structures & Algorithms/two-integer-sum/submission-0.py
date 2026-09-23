class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, 0,-1):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if i != j:  
                    return [j, i] 

