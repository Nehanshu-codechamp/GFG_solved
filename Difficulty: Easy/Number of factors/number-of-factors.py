class Solution:
    def countFactors (self, n):
     
    #  Yeh ek brute force approch hai, isko aur optimise kar sakta hu kya
     count = 0
     for i in range(1, n//2+ 1):
        if n % i == 0:
            count += 1
     count+=1        
     return count  




# the better solution hai ki mai loop (1 to n//2 +1 tak chaulau)

# aur optimal solution me loop (1, to sqt(num)+1) tak hi chalega