class Solution:
    def maxProduct(self, n: int) -> int:
        x=list(map(int,str(n)))
        m1=max(x)
        x.remove(m1)
        m2=max(x)
        return m1*m2
        # x=list(map(int,str(n)))
        # ans=0
        # k=len(x)
        # for i in range(k-1):
        #     ans=max(ans,x[i]*x[i+1])
        # return ans

