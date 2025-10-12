class Solution: 
    def solve(self, arr):
        n = len(arr)
        
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Swap
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    def selectionSort(self, arr):
        # Call helper function
        self.solve(arr)
        return arr




# class Solution: 
#     def solve(self,arr):
        
#         n = len(arr)
        
#     for i in range (0,n):
#          min_index =i
           
#          for j in range (i+1,n):
#               if arr[j]<arr[min_index]:
#                 min_index = j
            
#           arr[i],arr[min_index]=arr[min_index],arr[i]  
           
#     def selectionSort(self, arr):
#         #code here
#         self.solve(arr)