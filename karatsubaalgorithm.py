#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:18:49 2019

@author: amir
"""
import math

def karatsuba(x,y):
    if x<10 and y<10:
        return x*y
    else:
        n=math.log(x,10)
        nf=n//2+1
        a=int(x/10**(nf))
        b=int(x%10**(nf))
        c=int(y/10**(nf))
        d=int(y%10**(nf))
        ac=karatsuba(a,c)
        bd=karatsuba(b,d)
        adbc=karatsuba(a,d)+karatsuba(b,c)
        prod = ac * 10**(2*nf) + (adbc * 10**nf) + bd
        return int(prod)
