class Solution:
    def func(self, s, left, right):
        # Base case: if pointers cross, it's a palindrome
        if left >= right:
            return True
        
        # If mismatch found
        if s[left] != s[right]:
            return False
        
        # Recursive case
        return self.func(s, left + 1, right - 1)
    
    def isPalindrome(self, s):
        return self.func(s, 0, len(s) - 1)

# de   
#           return self.func(s,left+1,right-1)
#         #   recussive function
#     def isPalindrome(self, s): 
        
#         return self.func(s,0,len(s)-1)
#         # code heref func(self,s,left,right):
#       if left>= right:
#           return true
       
#       if s[left]!= s[right]:
#           return false
        
        