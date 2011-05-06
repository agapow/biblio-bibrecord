#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A collection of metadata in the Dublin Metadata Core format.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import metadata


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class DublinCoreCollection (metadata.MetadataCollection):
	pass

fields = (
	'contributor', 'coverage', 'creator', 'data', 'description', 'format',
	'identifier', 'language', 'publisher', 'relation', 'rights', 'source',
	'subject', 'title', 'type'
)

for f in fields:
	setattr (DublinCoreCollection, "%ss" %f,
		property (
			lambda s, v: s.set_value (f, v),
			lambda s: s.get_value (f),
			lambda s: s.del_value (f),
			"%s metadata" % f
		)
	)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################