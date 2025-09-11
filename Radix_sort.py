def radixsort(given_array: list[int])-> list[int]:

    radix_array = [[] for x in range(10)]
    maximum = max(given_array)
    exponent = 1

    while maximum // exponent > 0:

        while len(given_array) > 0:
            value = given_array.pop(0)
            radix_index = (value // exponent) % 10
            radix_array[radix_index].append(value)

        for bucket in reversed(radix_array):
            while len(bucket) > 0:
                value = bucket.pop()
                given_array.insert(0,value)
            
        exponent *= 10
    return given_array

print(radixsort([26,52,13,62]))