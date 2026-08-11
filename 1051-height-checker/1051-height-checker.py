class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        z=sorted(heights)
        c=0
        for i in range(len(z)):
            if heights[i]!=z[i]:
              c+=1
        return c    
        

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         n=len(heights)

#         c=0
#         expected=heights.copy()
#         for i in range(n-1):
#             for j in range(n-i-1):
#                 if expected[j] >expected[j+1]:
#                     expected[j],expected[j+1]=expected[j+1],expected[j]

#         for i in range(n):
#             if heights[i]!=expected[i]:
#                 c+=1
          
#         return c

        