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
	
	def __repr__ (self):
		return "foo"
		
	def __str__ (self):
		return self.__unicode__().encode ('ascii', 'replace')
		
	def __unicode__ (self):
		pairs = []
		for k, v in self.iteritems():
			if type(v) == types.ListType:
				v_str = u', '.join ([a.__repr__() for a in v])
			else:
				v_str = v.__unicode__()
			pairs.append (u"'%s': '%s'" % (k, v_str))
		pair_str = u", ".join(pairs)
		return u"{%s}" % pair_str
		
	def creators (self, role=None):
		if role:
			return [x for x in self['creator'] if x.attribs.get('role') == role]
		else:
			return self['creator']
			
	def authors (self):
		return self.creators(role='aut')

	def identifiers (self, scheme=None):
		if scheme:
			return [x for x in self['identifier'] if x.attribs.get('scheme') == scheme]
		else:
			return self['identifier']
			
	def isbn (self):
		return self.identifiers(scheme='ISBN')

	def dates (self, event=None):
		if event:
			return [x for x in self['date'] if x.attribs.get('event') == event]
		else:
			return self['date']
			
	def publication_date (self):
		return self.dates (event='publication')



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
