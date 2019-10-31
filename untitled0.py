# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:49:33 2019

@author: Rober
"""

import script1

from imp import reload
reload(script1)

import myfile
myfile.title

from myfile import title
title

import threenames

threenames.a, threenames.c

from threenames import a,b,c
a,b
dir(threenames)


import objecttypes
objecttypes



