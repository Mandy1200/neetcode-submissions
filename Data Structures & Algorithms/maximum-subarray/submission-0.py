class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currLen= nums[0]
        maxSum = nums[0]

        for i in range(1,len(nums)):

            currLen = max(nums[i],currLen+nums[i])
            maxSum = max(maxSum,currLen)

        return maxSum    