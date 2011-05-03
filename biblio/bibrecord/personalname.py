#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various utilities.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import re

import impl
import const


### CONSTANTS & DEFINES ###

AND_PAT = re.compile (r'\s+and\s+')
COMMA_SPLIT_RE = re.compile (r'\s*,\s*')


### IMPLEMENTATION ###

class PersonalName (impl.ReprMixin, impl.RawMixin):
	"""
	A name, as used for authors and editors.
	
	The terms 'given', 'other' and 'family' are used in preference to other
	schemes, as they are more culture-neutral and do not assume any particular
	ordering.
	
	given
		The first / christian or forename, e.g. 'John'.
	other
		Any middle names, e.g. 'James Richard'.
	family
		surname, last name, e.g. 'Smith'.

	"""
	# TODO: properties for 'middle', 'surname' etc.
	
	_repr_fields = [
		'prefix',
		'title',
		'given',
		'other',
		'family',
		'suffix',
	]
	
	def __init__ (self, given, other=None, family=None, title=None,
			prefix=None, suffix=None):
		"""
		C'tor, requiring only the given name.
		
		Note that the only required argument is the given name, allowing single
		names (e.g. 'Madonna'). Also the order of positional arguments allows a
		a regular name to be passed as 'John', 'James', 'Smith'. 
	
		"""
		self.given = given
		self.other = other
		self.family = family
		self.title = title
		self.prefix = prefix
		self.suffix = suffix
		
	def __unicode__ (self):
		"""
		Return a readable formatted version of the name.
		"""
		fields = [getattr (self, f, '') for f in self._repr_fields]
		return u' '.join ([f for f in fields if f])


def parse_single_name (name_str):
	"""
	Clean up an indivdual name into a more consistent format.
	
	:Parameters:
		name_str : string
			Text containing a single personal name, e.g. "Smith, Ted A."
	
	:Returns:
		The name parsed into a PersonalName object.
	
	Biblio data can be irregularly formatted. This is piece of pure heuristics
	that sniffs at a name and tries to parse it appropriately. This involves a
	fair amount of guesswork and blind faith. Note that it does not currently
	cope with titles, prefixes or suffixes. The original "raw" string is stored
	with the name for safety.
	
	"""
	family = given = other = ''
	# cleanup name and normalise space
	name_str = COLLAPSE_SPACE_RE.sub (' ', name_str.strip())
	# break into parts
	if (', ' in name_str):
		# if [family], [given] [other]
		name_parts = name_str.split (', ', 1)
		family = name_parts[0].strip()
		given_other = name_parts[1].split (' ', 1)
		given = given_other[0]
		other = given_other[1:]
	else:
		# if [given] [other] [family]
		name_parts = name_str.split (' ')
		given = name_parts[0]
		other_family = name_parts[1:]
		# the 'Madonna' clause
		if (other_family):
			family = other_family[-1]
			other = ' '.join (other_family[:-1])
	# some tidying up
	if (family.endswith ('.')):
		family = family[:-1]
	# create name
	name = PersonalName (given)
	name.family = family or ''
	name.other = other or ''
	name.raw = name_str
	## Postconditions & return:
	return name


def parse_names (name_str):
	"""
	Clean up a list of names into a more consistent format.

	:Parameters:
		name_str : string
			Text giving a series of names 
	
	:Returns:
		A list of the names parsed into PersonalName objects, e.g. "['Smith, A.
		B.', 'Jones, X. Y.']"

	This breaks up a list of names into individual names using some heuristics
	and then parses each indivdual name. We assume that names are seperated by
	"and" or some similar delimiter.
	
	For example::

		>>> n = parse_names ("Leonard Richardson and Sam Ruby.")
		>>> print (n[0].family == 'Richardson')
		True
		>>> print (n[0].given == 'Leonard')
		True
		>>> print (not n[0].other)
		True
		>>> n = parse_names ("Stephen P. Schoenberger, Bali Pulendran")
		>>> print (n[0].family == 'Schoenberger')
		True
		>>> print (n[0].given == 'Stephen')
		True
		>>> print (n[0].other == 'P.')
		True
		>>> n = parse_names ("Madonna")
		>>> print (not n[0].family)
		True
		>>> print (n[0].given == 'Madonna')
		True
		>>> print (not n[0].other)
		True
		
	"""
	## Preconditions & preparation:
	# clean up string and return trivial cases 
	name_str = name_str.strip()
	if (not name_str):
		return []
	# replace 'and'
	name_str = const.AND_PAT.sub (', ', name_str)
	## Main:
	auth_list = COMMA_SPLIT_RE.split (name_str)
	name_list = [parse_single_name (x) for x in auth_list]
	## Postconditions & return:
	return name_list


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
