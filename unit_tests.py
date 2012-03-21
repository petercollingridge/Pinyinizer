 #!/usr/bin/python
          # -*- coding: utf-8 -*-

""" Unit tests for pinyinizer.py """
import sys
sys.path.append("/..")

import pinyinizer

def getKnownValues(filename):
    """ Load file of known values for testing. """
    
    known_values = {}
    current_type = None
    
    with open(filename) as f:
        for line in f:
            if line.startswith('#'):
                current_type = line[2:].strip()
                known_values[current_type] = []
            else:
                if len(line)>2 and current_type:
                    known_values[current_type].append(tuple(line.strip().split('\t')))
                    
    return known_values
              
def runTests():
    known_values = getKnownValues("unit_tests_known_values.txt")
    
    passed = 0
    for test_type, test_set in known_values.iteritems():
        failures = []

        for (test_in, test_out) in test_set:
            result = pinyinizer.addToneMarks(test_in)
            if result != test_out:
                failures.append("   %s -> %s (expecting: %s)" % (test_in, result, test_out))
            else:
                passed += 1
                
        if failures:
            print ' In "%s", %d of %d failed:' % (test_type, len(failures), len(test_set))
            for failure in failures:
                print failure
            print   
            
    print "Passed %d tests" % passed
        
if __name__ == "__main__":
    runTests()
