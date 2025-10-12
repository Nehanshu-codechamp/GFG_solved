class Solution:
    def isPrime(self, n):
        # code here
        #  count =0 
        
        # for i in range (1,n + 1):
        #     if n%i == 0:
        #         count+=1
        # if count == 2:
        #         return True
        # else:
        #         return False   
        # optimise the code 
        
         # Handle edge cases
        if n <= 1:
            return False
        
        # Only check up to sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
