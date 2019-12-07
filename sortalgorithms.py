def mergesort(list0):
    n=len(list0)
    print(n)
    if n>2:
        mid= n//2
        a=list0[:mid]
        b=list0[mid:]
        asort=mergesort(a)
        bsort=mergesort(b)
        k=0
        sort=[]
        while k<n:
            if asort and bsort:
                if asort[0]<bsort[0]:
                    sort.append(asort[0])
                    asort.pop(0)
                else:
                    sort.append(bsort[0])
                    bsort.pop(0)
            elif not asort and bsort:
                sort.append(bsort[0])
                bsort.pop(0)
            elif not bsort and asort:
                sort.append(asort[0])
                asort.pop(0)
            else:
                break
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
