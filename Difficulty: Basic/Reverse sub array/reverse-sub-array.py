#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
	
      # Convert to 0-based indexing (GfG often uses 1-based)
        l -= 1
        r -= 1

        def helper(arr, left, right):
            # Base case
            if left >= right:
                return
            # Swap
            arr[left], arr[right] = arr[right], arr[left]
            # Recursive call
            helper(arr, left + 1, right - 1)

        helper(arr, l, r)
        return arr