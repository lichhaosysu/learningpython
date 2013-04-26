'''
Created on 2013-3-11

@author: Stefan
'''
def quicksort(array, low, high):
    i = low
    j = high
    temp = 0
    if low < high:
        temp = array[low]
        while i != j:
            while j > i and array[j] > temp:
                j = j - 1
            array[i] = array[j]
            while i < j and array[i] <= temp:
                i = i + 1
            array[j] = array[i]
        array[j] = temp
        quicksort(array, low, j - 1)
        quicksort(array, j + 1, high)

array = [49, 38, 35, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4,
                62, 99, 98, 54, 56, 17, 18, 23, 34, 35, 35, 49, 53, 34]
quicksort(array, 0, len(array) - 1)
print array
