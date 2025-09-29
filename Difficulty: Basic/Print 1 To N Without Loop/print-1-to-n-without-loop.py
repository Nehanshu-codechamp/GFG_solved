class Solution:    
    def printNos(self,n):
        #Code here
   
        # Base case
        if n == 0:
            return
        # Recursive call
        self.printNos(n - 1)
        print(n, end=" ")
#  this tail recurrsion