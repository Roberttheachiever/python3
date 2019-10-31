# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:13:48 2019

@author: Rober
"""

S = 'sp\xc4m'
S
S[2]

file = open('unidata.txt','w',encoding='utf-8')
S
file.write(S)
file.close

text = open('unidata.txt', encoding='utf-8').read()
text

len(text)

raw = open('unidata.txt','rb').read()
raw
len(raw)

text.encode('utf-8')
raw.decode('utf-8')

text.encode('latin-1')

text.encode('utf-16')

len(text.encode('latin-1')),len(text.encode('utf-16'))

import codecs
codecs.open('unidata.txt','rb').read()

open('unidata.txt','rb').read()
open('unidata.txt').read()
