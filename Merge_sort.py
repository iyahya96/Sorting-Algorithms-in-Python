
'''Merge sort is a sorting algorithm based on the divide-and-conquer paradigm
. It operates by recursively dividing an unsorted list into smaller sublists until each sublist contains only one element, which is inherently sorted.
Subsequently, these single-element sublists are repeatedly merged back together in a sorted manner to produce a fully sorted list.'''
#Main function
def merge_sort(nums: list[float])-> list[float]:

    #base cases/edge cases
    if not isinstance(nums,list):
        raise TypeError('All elements must be a list.')
    if len(nums) < 2:
        return nums.copy()
    if not all(isinstance(x,(int,float)) for x in nums):
        raise TypeError('All elements must be int or float.')

    #divide array in half and call fucntion recursively
    middle = len(nums) // 2
    left_side = nums[:middle]
    right_side = nums[middle:]
    sorted_left = merge_sort(left_side)
    sorted_right = merge_sort(right_side)
    return merge(sorted_left,sorted_right)

#helper function
def merge(first: list[float],second: list[float])-> list[float]:
    final_list = []
    i = j = 0
    while i <len(first) and j < len(second):
        if first[i] < second[j]:
            final_list.append(first[i])
            i += 1
        else:
            final_list.append(second[j])
            j += 1
    final_list.extend(first[i:])
    final_list.extend(second[j:])
    return final_list

#Driver code

print(merge_sort([3,6,1,7,14,17,4]))
