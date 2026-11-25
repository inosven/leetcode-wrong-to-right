# LC 15 3Sum
# https://leetcode.com/problems/3sum/
# 日期: 2026-11-25 | 章节: 双指针 | 结果: A | 用时: 15min

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1

            while left < right:
                target = -nums[i]
                cursum = nums[left] + nums[right]
                if cursum > target:
                    right-=1
                elif cursum < target:
                    left+=1
                elif  cursum == target:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return ans
