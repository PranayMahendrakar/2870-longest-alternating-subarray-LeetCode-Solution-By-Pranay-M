class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = -1
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1:
                length = 2
                expected = -1
                j = i + 2
                while j < n and nums[j] - nums[j - 1] == expected:
                    length += 1
                    expected *= -1
                    j += 1
                max_len = max(max_len, length)
        return max_len