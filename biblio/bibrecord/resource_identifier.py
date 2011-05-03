#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A unified class for storing structured identifiers, like ISBNs and URLS.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from impl import *

__all__ = [
	'ResourceIdentifier',
]


### IMPLEMENTATION ###

class ResourceIdentifier (ReprMixin):
	"""
	A unified class for storing structured identifiers, like ISBNs and URLS.
	
	Bibliographic data frequently needs to refer to identifiers in various
	schemes: ISBNs, SSNs, web addresses, etc. This class presents a universal
	interface for such schemes.
	
	"""
	def __init__ (self, scheme, id):
		"""
		Ctor, using a string representation of the ISBN.
		
		:Parameters:
			scheme : string
				The identification scheme or method
			id : string
				The identifier within the scheme or method.
		
		"""
		## Preconditions:
		# schemes are canonically lowercase
		scheme = scheme.lower().strip()
		# can't make same guarantee for id
		id = id.strip()
		# ensure we have a scheme and id
		assert_or_raise (scheme)
		assert_or_raise (id)
		
		## Main:
		self.scheme = scheme
		self.id = id
	
	def __unicode__ (self):
		return "%s (%s:%s)" % (self.__class__, self.scheme, self.id)


### END #######################################################################
