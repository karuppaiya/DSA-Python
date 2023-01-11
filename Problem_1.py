# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:02:40 2023

@author: karup
"""

import sys

class Solution:
    def minDist(self, arr, n, x, y):
        
        # idx1 and idx2 will store indices of
        # x or y and min_dist will store the minimum difference
        idx1=-1; idx2=-1; min_dist = sys.maxsize;
        for i in range(n) :
           # if current element is x then change idx1
           if arr[i]==x :
              idx1=i
              
           # if current element is y then change idx2
           elif arr[i]==y :
              idx2=i
           
           # if x and y both found in array
           # then only find the difference and store it in min_dist
           if idx1!=-1 and idx2!=-1 :
               min_dist=min(min_dist,abs(idx1-idx2));
               
        print(idx1,idx2)
        # if left or right did not found in array
        # then return -1
        if idx1==-1 or idx2==-1 :
            return -1
        # return the minimum distance
        else :
            return min_dist
    
    
    
ob = Solution()

arr = [96, 82, 48, 76, 34, 19, 7, 80, 36, 57, 77, 34, 19, 35, 5, 57, 16, 66, 42, 62, 89, 19, 60, 19, 25, 16, 20, 51, 77, 75, 12, 73, 8, 11, 100, 93, 81, 58, 72, 17, 14, 48, 2, 33, 82, 6, 41, 49, 72, 34, 10, 12, 53, 21, 30, 77, 36, 49, 79, 13, 75, 42]
n =len(arr)
x= 36
y= 33
print(ob.minDist(arr,n,x,y))


