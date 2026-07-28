class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        path = []

        visited = [False]*len(nums)
        
        def dfs():
            if len(nums) == len(path):
                result.append(path.copy())
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                visited[i] = True
                path.append(nums[i])

                dfs()

                path.pop()
                visited[i] = False

        dfs()
        return result                    