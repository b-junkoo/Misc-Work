# -*- coding: utf-8 -*-
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: Using recursion, True if char is in aStr; False otherwise
    '''
    if aStr == '' or len(aStr) == 1 and char != aStr:
        return False   
    testCharInd = round(len(aStr)/2) - 1
    testChar = aStr[testCharInd]
    if char == testChar:
        return True
    elif char > testChar:
        aStr = aStr[testCharInd+1:len(aStr)+1]
        return isIn(char, aStr)
    elif char < testChar:
        aStr = aStr[0:testCharInd]
        return isIn(char, aStr)
    
print(isIn('u', 'bbgloqr'))
