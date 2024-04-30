#Problem Link :- https://www.geeksforgeeks.org/problems/odd-or-even3618/1?page=2&difficulty=School&sortBy=submissions
class Solution:
    def oddEven (ob,N):
        if N == 1:
           return('odd')
        elif N % 2 == 0: 
            return('even')
        else:
            return('odd')
