#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various (fragile) implementation details and utilities.

Don't reply on these because they may go away.

"""
# TODO: error-handling logic is correct?

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import exceptions

__all__ = [
	'ReprMixin',
	'RawMixin',
	'assert_or_raise',
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class ReprMixin (object):
	"""
	A class with an simple and consistent printable version.
	
	This is pure development sugar, to ensure all classes are printable.
	"""
	
	_repr_fields = [
		# fields to be printed in representation
		# override in derived classes
	]
	
	def __str__ (self):
		return self.__unicode__().encode ('utf8')
	
	def __unicode__ (self):
		repr_strs = [u"%s: '%s'" % (field, getattr (self, field)) for field in
			self._repr_fields]
		return u"%s (%s)" % (self.__class__.__name__, u'; '.join (repr_strs))
	
	def __repr__ (self):
		return str (self)


class RawMixin (object):
	"""
	Provides objects with a 'raw' field for storing original values.
	
	Note that this does not need to be initialised in a subclass c'tor, the
	``raw`` attribute is created is it is used.
	"""
	
	def get_raw (self):
		return getattr (self, 'raw', None)
	
	def set_raw (self, value):
		self.raw = value
	
	raw = property (get_raw, set_raw, doc="the original value")


def assert_or_raise (cond, error_cls=exceptions.RuntimeError, error_msg=None):
	"""
	If a condition is not met, raise a assertion with this message.
	
	More developmental sugar.
	"""
	if (not cond):
		if error_msg:
			error = error_cls (error_msg)
		else:
			error = error_cls()
		raise error


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
