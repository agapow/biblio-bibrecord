Introduction
============

There's an obvious need for bibliographic records. At the same time, there's
a wide variety of different bibliographic standards. Amongst other issues, this
makes it difficult for software to inter-operate. Thus this module presents
common denominator data structures for representing bibliographic data,
including:

* books and publications
* identifiers likes ISBNs and DOIs
* personal names


Design philosophy
-----------------

This is one of those messy tasks that I would rather have avoided, but the
convergence of several different scripts for reading ebook metadata / fetching
bibdata from online servers / parsing identifiers made this inevitable. The rich
cacophony of standards means there is no hope of handling everything. Therefore,
we simply aim for reasonable interoperability of the most common information,
while trying to capture all passed information in some form. 

Bibliographic information is often inconsistently recorded. We try to extract or
convert information to a consistent form without throwing information away.

It's often useful to distinguish between cases where data or fields cannot be
found and when that data is empty. In the first case, we return ``None``, in the
second an empty record of some sort (e.g. string, dictionary).

As far as possible, we work in unicode.
