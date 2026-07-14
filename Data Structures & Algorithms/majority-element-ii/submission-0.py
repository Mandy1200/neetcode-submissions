class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        res = []

        for i in nums:
            dict[i] = dict.get(i,0)+1
        
        for i in dict:
            if dict[i] > len(nums)//3:
                res.append(i)
        
        return res