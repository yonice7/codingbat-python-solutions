# double_char
def double_char(str):
    '''
    Given a string, return a string where for every char in the original, there are two chars.
    '''
    word = ''
  
    for i in str:
        word += i * 2
    return word

# count_hi
def count_hi(str):
    '''
    Return the number of times that the string "hi" appears anywhere in the given string.
    '''    
    ctr = 0
    greet = 'hi'
  
    for i in range(len(str)-1):
        if str[i:i+2] == greet:
            ctr += 1
    return ctr

# cat_dog
def cat_dog(str):
    '''
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    '''
    cat = 'cat'
    dog = 'dog'
    ctr_cat = 0
    ctr_dog = 0
  
    for i in range(len(str)-2):
        if str[i:i+3] == cat:
            ctr_cat += 1
        if str[i:i+3] == dog:
            ctr_dog += 1
    return ctr_cat == ctr_dog

# count_code
def count_code(str):
    '''
    Return the number of times that the string "code" appears anywhere in the given string, 
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    '''
    code1 = 'co'
    code2 = 'e'
    ctr = 0
  
    for i in range(len(str)-3):
        if (str[i: i+2] == code1 and str[i+3] == code2):
            ctr += 1
    return ctr

# end_other
def end_other(a, b):
    '''
    Given two strings, return True if either of the strings appears at the very end of the 
    other string, ignoring upper/lower case differences (in other words, the computation 
    should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
    '''
    a = a.lower()
    b = b.lower()
  
    lstr = a
    sstr = b
  
    if len(b) > len(a):
        lstr = b
        sstr = a
  
    return lstr.endswith(sstr)

# xyz_there
def xyz_there(str):
    '''
    Return True if the given string contains an appearance of "xyz" where the xyz is not 
    directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    '''
    return str.count('xyz') - str.count('.xyz') > 0

