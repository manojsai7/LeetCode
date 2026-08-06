
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping={}
        used=set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                else:
                    mapping[s[i]]=t[i]
                    used.add(t[i])
        return True
"""
        if len(s)!=len(t):
            return False
        mapST={}
        mapTS={}
        for chS,chT in zip(s,t):
            if chS in mapST and mapST[chS]!=chT:
                return False
            if chT in mapTS and mapTS[chT]!=chS:
                return False
            mapST[chS]=chT
            mapTS[chT]=chS
        return True
"""