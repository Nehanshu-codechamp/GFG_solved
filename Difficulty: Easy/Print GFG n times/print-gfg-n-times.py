#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        # base case
        if n==0:
            return
        
        # reccursive fuc
        
        print ("GFG",end=" ")
        
        self.printGfg(n-1)