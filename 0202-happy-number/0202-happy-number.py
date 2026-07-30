class Solution:
    def getNext(self,n):
        total=0
        while n>0:
            dig=n%10
            total+=dig*dig
            n//=10
        return total
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n=self.getNext(n)
        return True
                