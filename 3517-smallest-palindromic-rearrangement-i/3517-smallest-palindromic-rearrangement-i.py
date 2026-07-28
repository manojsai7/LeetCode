class Solution:
    def smallestPalindrome(self, s: str) -> str:
        obj = Counter(s)
        res = ''
        mid = ''
        for i in obj:
            if obj[i]%2!=0:
                mid=i
            res+=(i)*(obj[i]//2)
        res = "".join(sorted(res))
        return res+mid+res[::-1] if res else mid
        