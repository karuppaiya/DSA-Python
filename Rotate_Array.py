# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:56:50 2023

@author: karup
"""

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        
        for i in range(0,D):
             first = A[0]
             
             for j in range(0,N-1):
                 A[j]=A[j+1]
                 
             A[N-1]=first
        return A
    
    
ob = Solution()

A = [1,2,3,4,5]
N =len(A)
D = 2
print(ob.rotateArr(A,D,N))



# Solution 2
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        
        D = D % N
        A[:] = A[D:] + A[:D]
        return A
    
A = [1,2,3,4,5]
N =len(A)
D = 2
print(ob.rotateArr(A,D,N))




