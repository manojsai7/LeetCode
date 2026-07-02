class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum,rsum,maxscore=0,0,0
        n=len(cardPoints)
        for i in range(k):
            lsum+=cardPoints[i]
        maxscore=lsum
        rIndex=n-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rIndex]
            rIndex-=1
            maxscore=max(maxscore,lsum+rsum)
        return maxscore

        