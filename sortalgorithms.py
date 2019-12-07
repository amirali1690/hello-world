def mergesort(list0):
    n=len(list0)
    if n>2:
        mid= n//2
        a=list0[:mid]
        b=list0[mid:]
        asort=mergesort(a)
        bsort=mergesort(b)
        k=0
        i=0
        j=0
        sort=[]
        while i<len(asort) and j<len(bsort):
            if asort[i]<bsort[j]:
                sort.append(asort[i])
                i+=1
            else:
                sort.append(bsort[j])
                j+=1
            k+=1
        while i<len(asort):
            sort.append(asort[i])
            i+=1
            k+=1
        while j<len(bsort):
            sort.append(bsort[j])
            j+=1
            k+=1
        return sort
    if n==1:
        return list0
    else:
        a=list0[0]
        b=list0[1]
        if a<b:
            return [a,b]
        else:
            return [b,a]


