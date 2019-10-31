# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 09:26:12 2019

@author: Rober
"""

S = 'Spam'
len(S)
S[0]
S[-1]
S[1:3]
S[1:]
S[:1]
S[:]
S + '123'
S = 'Z' + S[1:]
S
S = 'shruberry'
L=list(S)
L
L[1] ='c'
''.join(L)
L
B = bytearray(b'spam')
B.extend(b'eggs')
B
B.decode()
S = 'Spam'
S.find('pa')
S
S.replace('pa','XVZ')
S
line = 'aaa,bbb,cccc,dd'
line.split(',')

S ='spam'
S.upper()
S.isalpha()
line = 'aaa,bbb,ccccc,dd\n'
line.rstrip()
line.rstrip().split(',')
'%s eggs, and %s' %('spam','SPAM!')

'{0}, eggs, and {1}'.format('spam','SPAM')
'{}, eggs, and {}'.format('spam','SPAM')
'{:,.2f}'.format(296999.3567)

dir(S)
S + 'NI'
S
S.__add__('NI!')
S

S = 'A\nB\tC'
len(S)
ord('\n')
S='a\0b\0c'
len(S)
S










