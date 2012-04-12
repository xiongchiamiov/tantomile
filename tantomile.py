#!/usr/bin/env python

# May you recognize your weaknesses and share your strengths.
# May you share freely, never taking more than you give.
# May you find love and love everyone you find.

from pyquery import PyQuery
from stemming.porter2 import stem

url = 'http://beeradvocate.com/beer/profile/187/598'
q = PyQuery(url=url)
# This gets only reviews on the first page.
reviews = q('#mainContainer table').eq(1).find('td').eq(1).find('table').eq(2).find('tr').eq(3).children().children()

text = []
for review in reviews:
	words = q(review).text().split()
	# TODO: filter out common junk words
	# PyStemmer, while it is bindings to a C library (and thus, is probably
	# faster), has no documentation.  NLTK has docs but is gigantic.  So, the
	# simple stemming library it is.
	text.push(map(stem, words))

