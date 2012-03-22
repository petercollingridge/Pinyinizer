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


def replaceWithToneMarks(in_string):
    """ Replace piyin with tone numbers with tone marks. """
    
    def replaceToneNumber(match):
        letter = match.group(1)[0]
        number = int(match.group(2)) % 5
        return pinyin_tonemarks[letter][number] + match.group(0)[1:-1]
        
    def replaceVEWords(match):
        letter = match.group(1)
        number = int(match.group(2)) % 5
        return pinyin_tonemarks[letter][number] + match.group(0)[1:-2]

    in_string = re.sub(pinyin_re, replaceToneNumber, in_string)
    in_string = re.sub(pinyin_ue, replaceVEWords, in_string)
    
    return in_string
