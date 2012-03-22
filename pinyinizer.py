 #!/usr/bin/python
          # -*- coding: utf-8 -*-

import re

pinyin_re = re.compile('(?<!v)(a[io]?|ei?|[iou])(?:n|ng)?r?([0-5])')
pinyin_ue = re.compile('(ve?)([0-5])')

pinyin_tonemarks = {
    'a': ['a', 'ā', 'á', 'ǎ', 'à'],
    'e': ['e', 'ē', 'é', 'ě', 'è'],
    'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
    'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
    'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
    'v': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ'],
    've': ['üe', 'üē', 'üé', 'üě', 'üè']} 

""" Convert a string of pinyin with tone numbers
    to a string of pinyin with tone marks. """
    
def addToneMarks(in_string):
    """ Add tone marks to string of pinyin with tone numbers. """
    
    words = []
    for word in in_string.split(' '):
        match = pinyin_re.search(word)
        letter = None
        
        if match:
            letter, number = match.groups(0)
            letter = letter[:1]
            end = match.end() - 1
            
        else:
            match = pinyin_ue.search(word)
            if match:
                letter, number = match.groups(0)
                end = match.end() - 2

        if letter and pinyin_tonemarks.get(letter):
            tone_mark = pinyin_tonemarks[letter][int(number) % 5]
                
            start = match.start()
            word = word[:start] + tone_mark + word[start+1:end]
    
        words.append(word)
    
    out_string = ' '.join(words)
    return out_string
