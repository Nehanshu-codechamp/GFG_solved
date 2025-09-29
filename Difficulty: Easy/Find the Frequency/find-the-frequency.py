class Solution:
    def findFrequency(self, arr, x):
        freq_map = {}
        n = len(arr)
        
        for i in range(0,n):
            if arr[i] in freq_map:
                freq_map[arr[i]] += 1
            else:
                freq_map[arr[i]] = 1
        
        return freq_map.get(x, 0)
