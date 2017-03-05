# leetcode
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) > 0:

            U = set(range(1,len(nums)+1))
            A = set(nums)
            B = U - A

            return list(B)

        elif len(nums) <= 0:
            return []
