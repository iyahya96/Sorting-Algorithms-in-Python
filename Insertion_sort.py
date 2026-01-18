def insertion_sort(arr: list[float]) -> list[float]:
    arr = arr.copy()
    if not isinstance(arr,list):
        raise TypeError('All elements must be list.')
    if len(arr) < 2:
        return arr
    if not all(isinstance(x,int) for x in arr):
        raise TypeError('All elements must be int or float.')
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr
