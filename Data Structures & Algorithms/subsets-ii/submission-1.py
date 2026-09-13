class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(j, subset): 
            res.append(subset[::])

            for i in range(j, len(nums)): 
                if i > j and nums[i] == nums[i-1]: 
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0,[])
        return res
            