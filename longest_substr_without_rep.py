class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = -1
        result = 0
        c_dict = {}
        for i, element in enumerate(s):
            if element in c_dict and c_dict[element] > k:# 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[element]
                c_dict[element] = i
            else:
                c_dict[element] = i
                result = max(result, i - k)
        return result
