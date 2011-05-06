#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A unified class for storing structured identifiers, like ISBNs and URLS.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import types

from impl import *

__all__ = [
	'MetadataCollection',
	'MetadataValue',
]


### IMPLEMENTATION ###

class MetadataValue (ReprMixin):
	"""
	A field within a collection of metadata.
	
	This is used as a general representation for various pieces of meta- and
	structured data. Much (very much) like an XML tag, it has a single contained
	value and a set of attributes. Note that the name of the "tag" is not given as
	this is the *value*, which is stored against a name in the collection.
	"""
	
	def __init__ (self, value=None, attribs={}):
		self.value = value
		self.attribs = copy.deepcopy (attribs)
	
	def get_attrib (self, att, default=None):
		"""
		Return the value of the attribute with this name.
		
		Syntactic sugar.
		"""
		return self.attribs.get (att, default)


class MetadataCollection (dict):
	"""
	A set of metadata fields.
	
	This collection acts much like a dictionary, with metadata field names acting
	as keys to metadata values. Note this implementation assumes that order of
	metadata fields is irrelevant. If it is relevant, then you should be dealing
	with pure XML.
	
	It's difficult to choose the correct semantics for storing and returning
	values, as a naked item, a list or failure (no value) are all reasonable
	results. The scheme we follow is this: All values are stored and returned as
	lists - we make no assumptions about whether a given field should only have
	one value. Any setters will accept single items or lists. Any value type can
	be passed in but it will be stored as a MetadataValue.
	
	"""
	# TODO: should we implement properties?
	
	def __init__ (self, **kwargs):
		"""
		C'tor.
		
		If keyword arguments are passed, these are taken to be the names and
		values of the initial contents of the collection.
		"""
		self._contents = {}
		for k, v in kwargs.iteritems():
			self.set_value (k, v)
		
	def _convert_value (self, v):
		"""
		If the argument is not a MetadataValue, it is turned into one.
		
		Used for sanitizing the valuies stored in the collection. Not for external
		application.
		"""
		if type (v) != MetadataValue:
			v = MetadataValue (str(v))
		return v
		
	def set_value (self, f, v):
		"""
		Set the value(s) for a given metadata field, replacing any pre-existing.
		
		:Parameters:
			v : MetadataValue, String, List
				A single value or list of values. If values are not MetadataValues,
				they will be converted before storing.
				
		"""
		self._contents[f] = [self._convert_value(x) for x in make_list(v)]
		
	def append_value (self, f, v):
		"""
		Add value(s) for a given metadata field, appending to any pre-existing.
		
		:Parameters:
			v : MetadataValue, String, List
				A single value or list of values. If values are not MetadataValues,
				they will be converted before storing.
				
		This works whether there are any values for this field name or not.
		"""
		self.setdefault (key, []).extend (
			[self._convert_value(x) for x in make_list(v)]
		)
		
	def get_value (self, f):
		"""
		Return the value(s) for a given metadata field.
		
		Note that even if the field does not exist or has been emptied, an empty
		list be be returned, i.e. there is no error for a missing key.
		"""
		return self._contents.get (f, [])
		
	def del_value (self, f):
		"""
		Delete any value(s) for a given metadata field.
		
		Subsequent calls to this key will return an empty list.
		"""
		self._contents[f] = []
		
	def find_values (self, key, **kwargs):		
		# NOTE: should be a better way of doing this
		vals = []
		for v in self.get_value (key):
			for att, val in kwargs.iteritems():
				if v.get_attrib (att) == val:
					vals.append (v)
		return vals




### END #######################################################################
