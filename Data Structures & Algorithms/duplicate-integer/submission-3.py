class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = set()
        for n in nums:
            if n in number:
                return True 
            number.add(n)
        return False
