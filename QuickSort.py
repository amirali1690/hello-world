

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

def QuickSort(array,m):
    if len(array)==1:
        m=m+1
        print('case 1',array,m)
        return array,m
    elif len(array)==0:
        m=m+1
        return array,m
    elif len(array)==2:
        if array[0]>array[1]:
            temp=array[0]
            array[0]=array[1]
            array[1]=temp
            m=m+1
        m=m+1
        print('case2',array,m)
        return array,m
    else:
        pivot=array[0]
        array=array[1:]
        n=len(array)
        i,n=Partition(array,pivot)
        left=array[:i]
        right=array[i:]
        left1,ml=QuickSort(left,m)
        right1,mr=QuickSort(right,m)
        m=m+n+ml+mr
        print('casen',left,ml,right,mr,m)
        array=left1+[pivot]+right1
        return array,m
        