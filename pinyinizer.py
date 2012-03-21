 #!/usr/bin/python
          # -*- coding: utf-8 -*-

import re

pinyin_re = re.compile('(a[io]?|[ieouv])(?:n|ng)?r?([0-5])')

pinyin_tonemarks = {
	'a': ['a', 'ā', 'á', 'ǎ', 'à'],
	'e': ['e', 'ē', 'é', 'ě', 'è'],
	'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
	'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
	'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
	'v': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']} 

""" Convert a string of pinyin with tone numbers
	to a string of pinyin with tone marks. """
	
def addToneMarks(in_string):
	""" A tone marks to string of pinyin with tone numbers. """
	
	words = []
	for word in in_string.split(' '):
		match = pinyin_re.search(word)
		if match:
			letter, number = match.groups(0)
			letter = letter[:1]
			if pinyin_tonemarks.get(letter):
				n = int(number) % 5
				tone_mark = pinyin_tonemarks[letter][n]
				
				start = match.start()
				end = match.end()
				word = word[:start] + tone_mark + word[start+1:end-1]
		words.append(word)
	
	out_string = ' '.join(words)
	return out_string
