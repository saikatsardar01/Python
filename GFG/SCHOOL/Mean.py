# Problem Link :- https://www.geeksforgeeks.org/problems/mean0021/1?page=4&difficulty=School&sortBy=submissions

class Solution:
    def mean(self, N , A):
        S = 0
        k = len(A)
        for i in A:
            S = S+i
        mean = S//k
        return mean
