# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:24:10 2019

@author: Rober
"""
#multiple Target assignments
a=b=c='spam'
a

c = 'spam'
b=c
a=b
a

a=b=0
b=b+1
a,b

a=b=[]
b.append(42)
a,b

a=[]
b=[]
b.append(42)
a,b

a,b =[],[]

#agmented Assingnments
a *=5
a

L =[1,2]
L=L+[3]
L

L.extend([7,8])
L

L+=[9,10]
L

pwd