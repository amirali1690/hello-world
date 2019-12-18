#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:24:42 2019

@author: amir
"""

def countinv(list0):
    n=len(list0)
    if n>=2:
        mid= n//2
        l=list0[:mid]
        l0=list0[:mid]
        r=list0[mid:]
        r0=list0[mid:]
        invl=countinv(l)
        #print(l,invl)
        invr=countinv(r)
        #print(r,invr)
        k=0
        i=0
        j=0
        inv=0
        if invl:
            inv=inv+invl
        if invr:
            inv=inv+invr
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                list0[k]=l[i]
                i+=1
            else:
                list0[k]=r[j]
                j+=1
                inv=inv+len(l)-i
            k+=1
        while i<len(l):
            list0[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            list0[k]=r[j]
            j+=1
            k+=1
        return int(inv)
    elif len(list0)<2:
        inv=0
        return int(inv)

