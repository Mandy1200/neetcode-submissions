class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for i in nums:
            dict[i] = dict.get(i,0)+1
            if dict[i]>1:
                return True

        return False        