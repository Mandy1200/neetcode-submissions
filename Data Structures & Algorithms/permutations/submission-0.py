class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        visited = set()

        def dfs():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in visited:
                    continue
                visited.add(num)
                path.append(num)

                dfs()

                path.pop()
                visited.remove(num)

        dfs()
        return result        