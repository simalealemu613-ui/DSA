from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numscounter= Counter(nums)
        element, frequent=numscounter.most_common(1)[0]
        if frequent>= 2:
            return True
        return False
        # seen=set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)

        # return False
        