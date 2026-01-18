def bubble_sort(arr):
    if  not arr:
        return None
    if len(arr) == 1:
        return arr.copy()
    if not all(isinstance(x,(int,float)) for x in arr):
        raise TypeError('All elements must be int or float')
    arr = arr.copy()
    swaping = True
    end = len(arr)
    while swaping == True:
        swaping = False
        for i in range(1,end):
            if arr[i-1] > arr[i]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
                swaping = True
        end-=1
    return arr
