
def merge_sort(nums: list[float])-> list[float]:
    
    if not isinstance(nums,list):
        raise TypeError('All elements must be a list.')
    if len(nums) < 2:
        return nums.copy()
    if not all(isinstance(x,(int,float)) for x in nums):
        raise TypeError('All elements must be int or float.')
    
    middle = len(nums) // 2
    left_side = nums[:middle]
    right_side = nums[middle:]
    sorted_left = merge_sort(left_side)
    sorted_right = merge_sort(right_side)
    return merge(sorted_left,sorted_right)

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