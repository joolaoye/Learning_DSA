def quicksort(array):
    if len(array) < 2:
        return array

    r = len(array) - 1

    while array[0] > array[r]:
       array[0], array[r - 1] = array[r - 1], array[0]
       array[r - 1], array[r] = array[r], array[r - 1]


    return quicksort(array[:r]) + [array[r]] + quicksort(array[r+1:])


print(quicksort([8,7,6,1,0,9,2]))