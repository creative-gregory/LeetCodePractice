class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        target_dict = dict()

        for index, num in enumerate(nums):
            if (target - num) in target_dict:
                return [target_dict[target - num], index]

            else:
                target_dict[num] = index
