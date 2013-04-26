'''
Created on 2013-4-9

@author: Stefan
'''
import math
def radixsort(array):
    maxnum = array[0]
    for i in range(len(array)):
        if array[i] > maxnum:
            maxnum = array[i]
    time = 0
    while maxnum > 0:
        maxnum = maxnum / 10
        time = time + 1
    queue = [[] for i in xrange(10)]
    for i in range(time):
        for j in range(len(array)):
            x = array[j] % int(math.pow(10, i + 1)) / int(math.pow(10, i))
            queue[x].append(array[j])
        count = 0
        for k in range(10):
            while len(queue[k]) > 0:
                thislist = queue[k]
                array[count] = thislist[0]
                del thislist[0]
                count = count + 1
                
array = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4,
                62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51]
radixsort(array)
print array
