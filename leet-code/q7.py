from typing 
def containsDuplicate(self, nums: List[int]) -> bool:
        ls1 = []
        for i in nums:
            if nums[i] in ls1:
                return True
            else:
                print(ls1)
                ls1.append(nums[i])
        return False
