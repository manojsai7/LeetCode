class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Find if the two are equal
        if len(s)!=len(t):
            return False

        for char in set(s):
                if s.count(char)!=t.count(char):       
                    return False
        return True
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # return sorted(s)==sorted(t)
#         # c=0
#         # for i in s:
#         #     if i in s:
#         #         c+=1
#         # if len(s)==len(t)==c:
#         #     return True
#         # return False
        