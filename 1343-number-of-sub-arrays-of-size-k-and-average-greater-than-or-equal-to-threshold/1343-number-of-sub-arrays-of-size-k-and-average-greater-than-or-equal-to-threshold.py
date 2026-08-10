class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        winsum=sum(arr[:k])
        if winsum/k>=threshold:
            c+=1
        for i in range(k,len(arr)):
            winsum+=arr[i]-arr[i-k]
            if winsum/k>=threshold:
                c+=1
        return c
        