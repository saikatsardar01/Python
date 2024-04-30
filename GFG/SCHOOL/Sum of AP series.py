# Problem Link :- https://www.geeksforgeeks.org/problems/sum-of-ap-series4512/1?page=4&difficulty=School&sortBy=submissions

# Breaking the code into smaller parts help to understand the logic easily.

# The formula is  S = n/2(2a+(n-1)d)

class Solution:
	def sum_of_ap(self, n, a, d):
	    l = 2*a+(n-1)*d
	    k = n*l
	    S = k//2
	    return S
