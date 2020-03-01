import matplotlib.pyplot as plt


#n = number of eggs
#h = number of floors
def eggDropsRecursive(n,h):
    if(n==1 or h==1 or h==0):
        return h

    minDrops = 10**10

    #after you drop the egg at floor i if it breaks, there are eggDrops(n,)
    for i in range(1,h+1):
        minDrops = min(minDrops,1+max(eggDropsRecursive(n-1,i-1),eggDropsRecursive(n,h-i)))
    return minDrops

def eggDropsDynamic(n,h):
    eggDrops = [[0 for x in range(h+1)] for x in range(n+1)]

    for i in range(1,h+1):
        eggDrops[1][i]=i

    for i in range(1,n+1):
        eggDrops[i][0]=0
        eggDrops[i][1]=1

    minDrops = 10**10

    for numEggs in range(2,n+1):
        for numFloors in range(2,h+1):
            eggDrops[numEggs][numFloors] = 10**100
            for x in range(1,numFloors+1):
                const = 1+max(eggDrops[numEggs-1][x-1], eggDrops[numEggs][numFloors-x])
                if(const < eggDrops[numEggs][numFloors]):
                    eggDrops[numEggs][numFloors] = const
    return eggDrops[n][h]

def plotEggs1Var(n,x):
    #collect data n eggs, x samples
    drops = []
    for i in range(1,x+1):
        drops.append(eggDropsDynamic(n,i))
    return drops

def plotEggs2Var(n,x):
    #plot all eggs up to n with x samples
    for i in range(1,n+1):
        plt.title("Number of drops recquired for h floors and n eggs")
        plt.plot(plotEggs1Var(i,x))
    plt.show()


plotEggs2Var(10,100)




    #construct a matrix of eggDrops for n eggs and h floors
