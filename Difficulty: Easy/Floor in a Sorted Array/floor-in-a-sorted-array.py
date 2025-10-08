class Solution:
    def findFloor(self, arr, x):
        # code here
        # n= len(arr)-1
        # for i in range (n,-1,-1):
        #     if arr[i]<=x:
        #         break
        #     return i
       
        low, high = 0, len(arr) - 1
        Lower_bound = -1
        
        while low <= high:
            mid = (low + high) // 2
            # exact match
            if arr[mid] <= x:
                Lower_bound = mid   # possible floor
                low = mid + 1
            else:
                high = mid - 1
                
        return Lower_bound
