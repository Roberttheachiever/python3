# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:03:31 2019

@author: Rober
"""
D ={'food': 'Spam', 'quantity':4,'color':'pink'}
D['food']

D['quantity'] += 1
D

D={}
D['name']='Bob'
D['job'] = 'dev'
D['age'] =40
D

bob1 = dict(name='Bob', job = 'dev', age = 42)
bob2 = dict(zip(['name','job','age'],['bob','dev',45]))

#nesting visited
rec = {'name':{'last':'Bob', 'first':'Bob'},
       'job':['dev','mgr'],
       'age': 40}
rec

rec['name']
rec['name']['first']

rec['job'][1]

rec['job'].append('janitor')

rec

#missing keys
D={'a':1,'b':2,'c':3}
D['e'] = 99
#D['f']

'f' in D
if not 'f' in D:
    print('missing')
    print('no really...')

value = D.get('x',0)
value = D['a'] if 'a' in D else 0

D={'a':1,'b':2,'bc':3}
D
Ks = list(D.keys())
Ks

Ks.sort()
Ks

for key in Ks:
    print(key,'=>', D[key])
    
T = (1,2,3,4)
len(T)
T + (5, 6, 7)
T
T[0]

T.index(4)
T.count(4)

T =(2,) +T[1:]
T

T = 'spam',3.0,[11,22,33]
T



