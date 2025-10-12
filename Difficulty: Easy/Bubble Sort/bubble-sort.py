# class Solution:
#     def bubbleSort(self,arr):
#         # code here
#      n = len(arr)
        
#         for i in range(n - 1):   # n-1 passes
#             swapped = False      # to optimize if already sorted
            
#             for j in range(n - i - 1):  # last i elements are already sorted
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
#                     swapped = True
            
#             # if no swap happened, array is already sorted
#             if not swapped:
#                 break
        
#         return arr
class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        
        for i in range(0,n ):   # n-1 passes
            swapped = False      # to optimize if already sorted
            
            for j in range(0,n - i - 1):  # last i elements are already sorted
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                    swapped = True
            
            # if no swap happened, array is already sorted
            if swapped == False :
                break
        
        return arr
