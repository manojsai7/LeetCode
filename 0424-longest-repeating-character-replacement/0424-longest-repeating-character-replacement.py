class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        freq={}
        res=0
        for j in range(len(s)):
            if s[j] not in freq:
                freq[s[j]]=0
            freq[s[j]]+=1
            maxFreq=max(freq.values())
            curlen=j-i+1
            if curlen-maxFreq>k:
                freq[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res
