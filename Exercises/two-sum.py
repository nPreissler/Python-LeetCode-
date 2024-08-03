class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n, j in enumerate(range(len(nums))):
            for m, i in enumerate(range(len(nums))):
                if i == j:
                    break

                if (nums[n] + nums[i]) == target:
                    return [j, i]
                
#Difficulty : Easy