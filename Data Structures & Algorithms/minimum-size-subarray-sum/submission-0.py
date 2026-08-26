class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        minLen = float("inf")
        maxSum = 0

        for i in range(len(nums)):
            maxSum += nums[i]

            while maxSum >= target :
                minLen = min(minLen,i-l+1)
                maxSum -= nums[l]
                l += 1

        if minLen == float("inf"):
            return 0

        return minLen    