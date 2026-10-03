class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, path = [], []
        def back(start, remainder):
            if remainder == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > remainder:
                    break
                path.append(nums[i])
                back(i, remainder-nums[i])
                path.pop()
        back(0,target)
        return res