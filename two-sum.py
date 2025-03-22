class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Example 1:
        # Input: nums = [2,7,11,15], target = 9
        # Output: [0,1]
        # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        # Example 2:
        
        # Input: nums = [3,2,4], target = 6
        # Output: [1,2]
        # Example 3:
        
        # Input: nums = [3,3], target = 6
        # Output: [0,1]

        # Brute Force Solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        target_dict = dict()

        for index, num in enumerate(nums):
            difference = target - num
            
            if difference in target_dict:
                return [target_dict[difference], index]
            else:
                target_dict[num] = index

        # Example Flow
        # 1. Calculate the difference between the target and num[i]
        # 2A. If the difference is not in the dict add the difference as the key and the index as the value
        # 2B. If the difference is in the dict return the index value stored in the dict and the current index

        # Example 1 Flow
        # Difference: 9 - 2 == 7 
        # Is 7 in the dict? no, add 7 to the dict as key and index == 0 as value
        # Difference: 9 - 7 == 2
        # Is 2 in the dict? yes return [taget_dict[num], index]
