class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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