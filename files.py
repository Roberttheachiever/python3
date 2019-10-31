# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:44:19 2019

@author: Rober
"""

f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close() 

f = open('data.txt')
text = f.read()
text
print(text)

text.split()

for line in open('data.txt'): print(line)

dir(f)

