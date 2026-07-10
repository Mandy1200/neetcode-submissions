class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        res = [0]*(2*leng)
    
        for i in range(leng):
            res[i] = nums[i]
            res[i+leng] = nums[i]

        return res    
