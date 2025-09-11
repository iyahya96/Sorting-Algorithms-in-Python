'''def count_sort(original_array:list[int])-> list[int]:

    maximum_number = max(original_array)
    count_array = [0] * (maximum_number + 1)

    while len(original_array) > 0:
        num = original_array.pop(0)
        count_array[num] += 1

    for j in range(len(count_array)):
        while count_array[j] > 0:
            original_array.append(j)
            count_array[j] -= 1
    return original_array'''


'''Counting sort is an efficient, non-comparison based sorting algorithm particularly well-suited for sorting a collection of objects according to keys that are small, non-negative integers.
It operates by determining the position of each element in the output array by counting the occurrences of each unique key value.'''
def count_sort(given_array:list[int])->list[int]:

    #determine max
    maximum_number = max(given_array)
    #initialize counting array
    count_array = [0] * (maximum_number + 1)

    #Store Frequency
    for i in given_array:
        count_array[i] += 1
    
    #Cumulative Sum
    for i in range(1,len(count_array)):
        count_array[i] += count_array[i-1]

    count_array = [0] + count_array[:-1]
    #initialize output array
    output = [0] * len(given_array)

    #build output array
    for i in given_array:
        output[count_array[i]] = i
        count_array[i] += 1
    return output

print(count_sort([1,0,3,1,3,1]))
