# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 12:07:37 2019

@author: Rober
"""

'sp\xc4m'

b'a\x01c'

u'sp\u00c4m'

print(u'sp\xc4m')

b'a\x01c'

b'a\x01c'


'spam'

'spam'.encode('utf8')

'spam'.encode('utf16')

'sp\xc4\u00c4\U000000c4m'

'\u00A3','\u00A3'.encode('latin1'), b'\xA3'.decode('latin1')

u'x' + b'y'
u'x' + 'y'

'x' + b'y'.decode()
'x'.encode() + b'y'
