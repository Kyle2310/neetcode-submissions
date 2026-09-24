class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = set()
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num]+=1
        sorted_freq = sorted(num_dict.values(), reverse = True)
        for i in range(k):
            for key,value in num_dict.items():
                if value == sorted_freq[i]:
                    result.add(key)
        return list(result)
            