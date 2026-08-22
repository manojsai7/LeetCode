class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # if len(n)==1 or len(n)==0:
        #     return False
        # if n<10:
        #     return False
        # if n%10==0:
        #     return True
        # if n==42:
        #     return True
        m=n
        summ=0
        mul=1
        while m>0:
            rem=m%10
            mul*=rem
            summ+=rem
            m=m//10
        return n%(mul+summ)==0
            
        
        