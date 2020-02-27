def withDivision(nums):
    #O(n) complexity as no nested for loops
    product = 1
    prods = []
    for n in nums: product*=n
    for n in nums: prods.append(int(product/n))
    print(prods)
    return prods

def noDivision(nums):
    #O(n^2) complexity as one nested for loop
    prods = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if(j!=i):
                product*=nums[j]
        prods.append(product)
    print(prods)
    return prods

def fastNoDivision(nums):
    #no nested for loops, O(n) complexity
    rightProds,leftProds,outProds = [],[],[]
    p = 1
    for i in range(len(nums)):
        p*=nums[i]
        rightProds.append(p)
    print(rightProds)
    p = 1
    for i in range(len(nums)):
        p*=nums[len(nums)-1-i]
        leftProds.append(p)
    print(leftProds)
    for i in range(len(nums)-1):
        if(i==0): outProds.append(leftProds[len(nums)-2])
        if(i==len(nums)-2): outProds.append(rightProds[len(nums)-2])
        else:
            print(leftProds[i+1], rightProds[i-1])
            outProds.append(leftProds[i+1]*rightProds[i-1])
    print(outProds)
    return outProds

fastNoDivision([1,2,3,4,5])
