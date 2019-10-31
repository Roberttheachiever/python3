
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:39:49 2019

@author: Rober
"""

X = set('spam')
Y = {'h','a','m'}
X,Y

X & Y

X|Y

X-Y

X>Y

{n ** 2 for n in [1,2,3,4]}

list(set([1,2,3,4]))

list(set([1,2,1,3,2,4,]))

set('spam') - set('ham')

set('spam') == set('ham')

'p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs','spam','ham']


import decimal
d = decimal.Decimal('3.14159')
d+1

decimal.getcontext().prec = 2
decimal.Decimal('1.00')/ decimal.Decimal('3.00')

from fractions import Fraction
f = Fraction(2,3)
f + 1
f + Fraction(1,2)

#boolean
1>2, 1<2

bool('spam')

X = None
print(X)

L = [None] * 100
L

type(L)

if type(L) ==([]):
    print('yes')
    
if type(L) ==list:
    print('yes')
    
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        
bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
bob.lastName()
sue.giveRaise(.10)
sue.pay




