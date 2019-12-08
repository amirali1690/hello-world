def mergesort(list0):
    n=len(list0)
    if n>=2:
        mid= n//2
        l=list0[:mid]
        r=list0[mid:]
        mergesort(l)
        mergesort(r)
        k=0
        i=0
        j=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                list0[k]=l[i]
                i+=1
            else:
                list0[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            list0[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            list0[k]=r[j]
            j+=1
            k+=1



def merge_sort(array):
    if (len(array)>=2):
        iM = len(array)//2
        
        left = array[:iM].copy()
        right = array[iM:].copy()
        
        merge_sort(left)
        merge_sort(right)
        
        iA = 0
        iB = 0
        iC = 0
        
        while(iA<len(left) and iB<len(right)):
            if left[iA]<right[iB]:
                array[iC]=left[iA]
                iA+=1
            else:
                array[iC]=right[iB]
                iB+=1
            iC+=1
            
        while(iA<len(left)):
            array[iC]=left[iA]
            iA+=1
            iC+=1
            
        while(iB<len(right)):
            array[iC]=right[iB]
            iB+=1
            iC+=1