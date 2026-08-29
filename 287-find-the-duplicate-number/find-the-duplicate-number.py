class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                return i
        