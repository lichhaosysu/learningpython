'''
Created on 2013-3-8

@author: Stefan
'''
def insertsort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp

array = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4,
                62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51]
insertsort(array)
print array
