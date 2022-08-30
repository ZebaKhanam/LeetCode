class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for m in range(length-1):
            for n in range(m+1,length):
                if nums[m] + nums[n] == target:
                    return [m,n];
            
        
