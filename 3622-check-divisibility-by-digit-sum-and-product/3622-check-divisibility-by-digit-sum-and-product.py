class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m=n
        summ=0
        mul=1
        while m>0:
            rem=m%10
            mul*=rem
            summ+=rem
            m=m//10
        return n%(mul+summ)==0
            
        
        