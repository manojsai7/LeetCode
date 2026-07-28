class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        first=strs[0]
        for i in range(len(first)):
            for word in strs[1:]:
                if i>=len(word) or word[i]!=first[i]:
                    return ans
            ans+=first[i]
        return ans
        