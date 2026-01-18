
'''Counting sort is an efficient, non-comparison based sorting algorithm particularly well-suited
for sorting a collection of objects according to keys that are small, non-negative integers.
It operates by determining the position of each element in the output array by counting the
occurrences of each unique key value.'''

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
