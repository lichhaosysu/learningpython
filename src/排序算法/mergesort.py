'''
Created on 2013-4-1

@author: Stefan
'''
def merge(R, low, mid, high):
    size = high - low + 1
    R1 = [ 0 for I in range(0, size)]
    i = low
    j = mid + 1
    k = 0
    while i <= mid and j <= high:
        if R[i] <= R[j]:
            R1[k] = R[i]
            i = i + 1
            k = k + 1
        else:
            R1[k] = R[j]
            j = j + 1
            k = k + 1
            
    while i <= mid:
        R1[k] = R[i]
        i = i + 1
        k = k + 1
        
    while j <= high:
        R1[k] = R[j]
        j = j + 1
        k = k + 1
        
    k = 0
    for i in range(low, high + 1):
        R[i] = R1[k]
        k = k + 1
        

def mergepass(R, length, n):
    i = 0
    while i + 2 * length - 1 < n:
        merge(R, i, i + length - 1, i + 2 * length - 1)
        i = i + 2 * length
    
    if i + length - 1 < n:
        merge(R, i, i + length - 1, n - 1)
        
def frombottomtotopmergesort(R, n):
    length = 1
    while length < n:
        mergepass(R, length, n)
        length = 2 * length

def fromtoptobottommergesort(R, low, high):
    mid = 0
    if low < high:
        mid = (low + high) / 2
        fromtoptobottommergesort(R, low, mid)
        fromtoptobottommergesort(R, mid + 1, high)
        merge(R, low , mid, high)
        
R = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4,
                62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51]

fromtoptobottommergesort(R, 0, len(R) - 1)

print 'fromtoptobottommergesort: ', R

R = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4,
                62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51]

frombottomtotopmergesort(R, len(R))

print 'frombottomtotopmergesort: ', R
