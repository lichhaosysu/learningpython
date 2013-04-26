'''
Created on 2013-3-3

@author: Stefan
'''
def bubblesort(array):
    temp = 0 
    length = len(array)
    for i in range(length - 1):
        for j in reversed(range(i + 1, length)):
            if(array[j] < array[j - 1]):
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp

array = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4,
                62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51]
bubblesort(array)
print array
