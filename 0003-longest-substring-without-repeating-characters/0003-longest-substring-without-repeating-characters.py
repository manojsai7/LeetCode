# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charset=set()
#         n=len(s)
#         l,r,maxlen=0,0,0
#         while r<n:
#             if s[r] not in charset:
#                 charset.add(s[r])
#                 maxlen=max(maxlen,r-l+1)
#                 r+=1
#             else:
#                 charset.remove(s[l])
#                 l+=1
#         return maxlen
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores last seen index of each character
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1  # move left past duplicate

            char_index[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len