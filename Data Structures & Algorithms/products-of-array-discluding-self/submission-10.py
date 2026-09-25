import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        list_prod = math.prod(nums)
        is_zero_dict = {}
        zero_count = nums.count(0)
        if zero_count == 0:
            for num in nums:
                result.append(int(list_prod/num))
        elif zero_count == 1:
            no_zero_nums = nums.copy()
            no_zero_nums.remove(0)
            prod_for_zero = math.prod(no_zero_nums)
        if zero_count == 1:
            for num in nums:
                if num == 0:                 
                    result.append(prod_for_zero)
                else:
                    result.append(0)
        if zero_count > 1:
            for num in nums:
                result.append(0)
        return result