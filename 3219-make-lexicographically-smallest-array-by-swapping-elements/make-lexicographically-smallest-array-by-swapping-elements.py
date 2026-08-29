from collections import defaultdict

class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        
        # Step 1: Sort nums with indices
        arr = sorted([(val, i) for i, val in enumerate(nums)])
        
        # Step 2: Group indices based on limit
        groups = []
        current_group = [arr[0][1]]
        
        for i in range(1, n):
            if arr[i][0] - arr[i-1][0] <= limit:
                current_group.append(arr[i][1])
            else:
                groups.append(current_group)
                current_group = [arr[i][1]]
        groups.append(current_group)
        
        # Step 3: Sort values within each group and place back
        res = nums[:]
        for g in groups:
            values = sorted(nums[i] for i in g)
            for idx, val in zip(sorted(g), values):
                res[idx] = val
        
        return res
