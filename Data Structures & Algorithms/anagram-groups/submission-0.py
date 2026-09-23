class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_dict = {}
        copy_strs = strs.copy()
        for i in range(len(copy_strs)):
            copy_strs[i] = ''.join(sorted(copy_strs[i]))
        for i in range(len(copy_strs)):
            if copy_strs[i] not in anagram_dict:
                anagram_dict[copy_strs[i]] = [i]
            else:
                anagram_dict[copy_strs[i]].append(i)
        for value in anagram_dict.values():
            sublist = []
            for index in value:
                sublist.append(strs[index])
            result.append(sublist)
        return  result

