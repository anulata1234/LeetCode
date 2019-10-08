class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old_num = {}
        for i in range(len(nums)):
            if old_num.get(target - nums[i]) is not None:
                return [old_num.get(target - nums[i]) , i ]
            else:
                old_num[nums[i]] = i
                
sum_index = Solution()
sum_index.twoSum([2,7,11,15],9)
