class Solution:
    def largest(self, arr):
        # code here
        
    #   largest = arr[0]
      largest = float("-inf")
      n = len(arr)
      
      for i in range (0,n):
          largest = max(largest, arr[i]) 
        #   if arr[i]> largest:
        # largest =arr[i]  yaha ye bhi use kar sakte hai
      return largest
    # method 1
    
    
    # method 2
    # largest = float("-inf")