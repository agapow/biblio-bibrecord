from setuptools import setup, find_packages
import os

version = '0.1'

setup(
	name='biblio-bibrecord',
	version=version,
	description="Data structures for representing bibliographic data",
	long_description=open("README.txt").read() + "\n" +
		open(os.path.join("docs", "HISTORY.txt")).read(),
	# TODO: get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		"Programming Language :: Python",
	],
	keywords='bibliographic metadata records',
	author='Paul-Michael Agapow',
	author_email='pma@agapow.net',
	url='http://www.agapow.net/software/biblio-bibrecord',
	license='GPL',
	packages=find_packages(exclude=['ez_setup']),
	namespace_packages=['biblio'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'setuptools',
		# -*- Extra requirements: -*-
	],
	entry_points="""
		# -*- Entry points: -*-
	""",
)
