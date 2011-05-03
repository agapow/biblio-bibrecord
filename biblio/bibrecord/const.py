#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various module-wide constants.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import re

import const

__all__ = [
	'COLLAPSE_SPACE_RE',
]


### CONSTANTS & DEFINES ###

COLLAPSE_SPACE_RE = re.compile (r'\s+')


### IMPLEMENTATION ###

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
