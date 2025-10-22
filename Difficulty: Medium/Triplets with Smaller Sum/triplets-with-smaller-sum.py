class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        arr.sort()
        ans = 0
        n = len(arr)
        for i in range(0,n-2):
            
            left = i +1
            right = n-1
            
            while left < right:
                add = arr[i] + arr[left] + arr[right]
                
                if (add>= sum):
                    right -=1
                else: # add<sum ye line main because we use thois line to take expected output
                    ans = ans + (right - left)
                    left +=1
        return ans            