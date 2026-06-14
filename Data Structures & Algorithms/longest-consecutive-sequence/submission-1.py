class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest sequence length
        longest = 0

        # set to track each number
        numSet = set(nums)

        for n in nums:
            # check if number is start of the sequence - has no left neighbor
            if (n-1) not in numSet:
                length = 0
                # find numbers to right of starting point
                while (n + length) in numSet:
                    length += 1
                # update longest
                longest = max(length, longest)
        
        return longest