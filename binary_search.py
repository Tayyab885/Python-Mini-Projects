def binarySearch(l,target,low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    
    if high < low:
        return -1
    
    midpoint = (low+high)//2
    
    if l[midpoint] == target:
        return midpoint

    elif target < l[midpoint]:
        return binarySearch(l,target,low,midpoint-1)
    else:
        return binarySearch(l,target,midpoint+1,high)
if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    target = 7
    print(binarySearch(l,target))
