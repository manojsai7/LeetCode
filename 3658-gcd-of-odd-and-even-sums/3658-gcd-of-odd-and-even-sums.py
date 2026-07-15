class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        os,es=0,0
        for i in range(n):
            os+=2*i+1
            es+=2*i+2
        print(os,es)
        while es!=0:
            os,es=es,os%es
        return os
            #     for i in range(1,n+1):
            # if i%2!=0:
            #     os+=i
            # else:
            #     es+=i
        # odds=[x for x in range(1,n+1) if x%2!=0]
        # even=[x for x in range(2,n+1) if x%2 ==0]

        