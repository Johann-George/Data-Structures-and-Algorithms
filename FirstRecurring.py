class firstRecurring:
    def firstRecurring(self,nums):
        arr=[]
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
            else:
                return nums[i]
        return None

first= firstRecurring()
print(first.firstRecurring([2,5,1,2,3,5,1,2,4]))
