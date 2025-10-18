class Solution:
    def frequencyCount(self, arr):
        freq_map = {}
        n = len(arr)
        
        for i in range(n):
            if arr[i] in freq_map:
                freq_map[arr[i]] += 1
            else:
                freq_map[arr[i]] = 1
        # result = []
        
        # # To return the full frequency dictionary:
        # for i in range(1, n + 1):
        #     if i in freq_map:
        #         result.append(freq_map[i])
        #     else:
        #         result.append(0)

        # return result
        
        for i in range(1, n + 1):
            if i in freq_map:
                arr[i - 1] = freq_map[i]
            else:
                arr[i - 1] = 0

        return arr
