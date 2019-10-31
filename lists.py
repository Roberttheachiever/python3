# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:28:20 2019

@author: Rober
"""

L = [123,'spam', 1.23]
len(L)

L*2
L

#typical specic operations
L.append('NI')
L

L.pop(2)
L

M = ['bb','aa','cc']
M.sort()
M

M.reverse()
M

#Bound checking
L

L[99]

L[99] = 1

#Nesting
M=[[1,2,3],[4,5,6],[7,8,9]]
M
M[1][2]

#Comprehension
col2 = [row[1] for row in M]
col2 

[row[1] + 1 for row in M]

[row[1] for row in M if row[1] % 2==0]

diag = [M[i][i] for i in [0,1,2]]
diag

doubles = [c * 2 for c in 'spam']
doubles

list(range(4))


list(range(-6,7,2))

[[x**2,x**3] for x in range(4)]

[[x,x/2,x*2] for x in range(-6,7,2) if x>0]

G = (sum(row) for row in M)
next(G)
next(G)
next(G)

list(map(sum,M))

{sum(row) for row in M}
{i : sum(M[i]) for i in range(3)}

[ord(x) for x in 'spaam']

{ord(x) for x in 'sppam'}

{x: ord(x) for x in "spaam"}


(ord(x) for x in 'spaam')


