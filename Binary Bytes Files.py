# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:58:14 2019

@author: Rober
"""

import struct
packed = struct.pack('>i4sh',7, b'spam', 8)
packed

file =open('data.bin','wb')
file.write(packed)
file.close

data= open('data.bin','rb').read()
data
data[4:8]
list(data)
struct.unpack('>i4sh',data)

