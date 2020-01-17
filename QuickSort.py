

import csv

data = open('PR.txt', 'r')
reader = csv.reader(data)
data1=[]
for row in reader:
    data1.append(int(row[0]))
    

def Partition(array,pivot):
    i=0
    for k in range(len(array)):
        if array[k]<pivot:
            temp=array[k]
            temp0=array[i]
            array[i]=temp
            array[k]=temp0
            i+=1
    return i

    
def QuickSort2(array,m):
    if len(array)<2:
        if len(array)>0:
            m=m+len(array)-1
        return array,m
    else:
        pivot=array[0]        
        array=array[1:]
        i=Partition(array,pivot)
        left = array[:i]
        right = array[i:]
        if left:
            if left[-1]>pivot:
                m=m+1
        left,ml=QuickSort2(left,m)
        right,mr=QuickSort2(right,m)
        m=m+ml+mr+len(array)

        array=left+[pivot]+right
        return array,m