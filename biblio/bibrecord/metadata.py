#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A unified class for storing structured identifiers, like ISBNs and URLS.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from impl import *

__all__ = [
	'MetadataCollection',
	'MetadataValue',
]


### IMPLEMENTATION ###

class MetadataCollection (dict):
	"""
	A set of metadata fields.
	
	This collection acts much like a dictionary, with metadata field names acting
	as keys to metadata values. For convenience, methods are provided for
	appending values (i.e. adding to a list of values for a given key), and
	finding values based on key and attributes.
	
	Note this implementation assumes that order of metadata fields is irrelevant.
	If it is relevant, then you should be dealing with pure XML.
	
	It's a bit difficult to know the correct semantics for returning values, as
	a naked item, a list or failure are all valid results, making for 
	
	"""
	
	def __repr__ (self):
		return "foo"
		
	def append (self, key, val):
		self.setdefault (key, []).append (val)
	
	def get_as_list (self, key, default=[]):
		val = self.get (key, None)
		if key and (type(key) != ListType):
			return [key]
		else:
			return default
		
	def find_values (self, key, **kwargs):
		for v in self.get_as_list (key):
			for att, val in kwargs.iteritems():
				if v.get_attrib (att) == val:
					return v


class MetadataValue (ReprMixin):
	"""
	A field within a collection of metadata.
	
	This is used as a general representation for various pieces of meta- and
	structured data. Much (very much) like an XML tag, it has a single contained
	value and a set of attributes.
	
	"""
	
	def __init__ (self, value=None, attribs={}):
		self.value = value
		self.attribs = copy.deepcopy (attribs)
	
	def get_attrib (self, att, default=None):
		return self.attribs.get (att, default)



### END #######################################################################
