def missingIntSlow(nums):
    #find first missing positive integer in array of positive numbers
    small = 1
    nums.sort()
    for n in nums:
        if(small==n):
            small+=1
    return small
    #sorting takes nlog(n), loop takes n so O(nlogn)

def missingIntFast(nums):
    size = len(nums)
    for i in range(len(nums)):
        n = abs(nums[i])
        if(abs(n)-1<size):
            nums[n-1] *=-1
    for i in range(len(nums)):
        if(nums[i]>0): return i+1
    return size+1


print(missingIntFast([3,4,-1,1]))
