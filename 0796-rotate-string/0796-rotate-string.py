class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        t=list(s)
        if len(s)!=len(goal):
            return False
        for i in range(len(t)):
            first=t.pop(0) # t.insert(len(t)-1,i)
            t.append(first)# t.pop(i)
            if "".join(t)==goal:
                return True
        return False

        