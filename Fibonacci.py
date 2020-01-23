#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:35:44 2020

@author: amir
"""

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        result=[1,1]
        while n>2:
            temp=result[0]+result[1]
            result[0]=result[1]
            result[1]=temp
            n=n-1
        return temp
    