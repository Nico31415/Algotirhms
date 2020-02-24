import time
import random

def twoSum(nums,target):
    complementMap = dict()
    for i in range(len(nums)):
        num = nums[i]
        if(num in complementMap):
            return([complementMap[num],i])
        else:
            complementMap[target-num]=i

print(twoSum([2,3,5,7],8))
