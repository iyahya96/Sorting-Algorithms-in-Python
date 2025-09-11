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


#Driver code
print(bubble_sort([1.2,3.5,0.1,8.7]))              # Floats 
print(bubble_sort([5, 5, 5, 5]))                   # Identical elements
print(bubble_sort([1, 2, 3, 4, 5]))                # Already sorted
print(bubble_sort([5, 4, 3, 2, 1]))                # Descending order
print(bubble_sort([-3, -1, -2, 0, 2]))             # Negative numbers
print(bubble_sort([2, 3, 2, 1, 3]))                # Duplicates
print(bubble_sort([]))                             # Empty list
print(bubble_sort([42]))                           # Single element
#print(bubble_sort([1, "a", 3]))                  # Uncomment to see TypeError