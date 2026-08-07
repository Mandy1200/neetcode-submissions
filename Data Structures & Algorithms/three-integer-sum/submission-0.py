class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for l in range(len(nums)):

            if l > 0 and nums[l] == nums[l - 1]:
                continue

            m = l + 1
            r = len(nums) - 1

            while m < r:

                tot = nums[l] + nums[m] + nums[r]

                if tot == 0:

                    res.append([nums[l], nums[m], nums[r]])

                    while m < r and nums[m] == nums[m + 1]:
                        m += 1

                    while m < r and nums[r] == nums[r - 1]:
                        r -= 1

                    m += 1
                    r -= 1

                elif tot < 0:
                    m += 1

                else:
                    r -= 1

        return res