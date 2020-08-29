# string_times
def string_times(str, n):
    '''
    Given a string and a non-negative int n, return a larger string that is n copies of 
    the original string.
    '''
    n_str = str * n
    return n_str

# front_times
def front_times(str, n):
    '''
    Given a string and a non-negative int n, we'll say that the front of the string is the 
    first 3 chars, or whatever is there if the string is less than length 3. Return n copies 
    of the front;
    '''
    n_str = str[0:3] * n
    return n_str

# string_bits
def string_bits(str):
    '''
    Given a string, return a new string made of every other char starting with the first, 
    so "Hello" yields "Hlo".
    '''
    result = ""
  
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result  

# string_splosion
def string_splosion(str):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    '''
    result = ""
  
    for i in range(len(str)+1):
        result = result + str[:i]
    return result

# last2
def last2(str):
    '''
    Given a string, return the count of the number of times that a substring length 2 appears
    in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't 
    count the end substring).
    '''
    ctr = 0
    checkStr = str[len(str) - 2: len(str)]
  
    for i in range(len(str) - 2):
        if str[i:i + 2] == checkStr:
            ctr +=  1
    return ctr

# array_counts
def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.
    '''
    n = list(nums)
  
    return n.count(9)

# array_front9
def array_front9(nums):
    '''
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
    The array length may be less than 4.
    '''
    n = list(nums)
  
    return 9 in n[0:4]

# array123
def array123(nums):
    '''
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array
    somewhere.
    '''
    numbers = list(nums)
    array = [1,2,3]
  
    for i in range(len(numbers) - 2):
        if numbers[i: i + 3] == array:
            return True
    return False

# string_match
def string_match(a, b):
    '''
    Given 2 strings, a and b, return the number of the positions where they contain the same length 
    2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings 
    appear in the same place in both strings.
    '''
    count = 0
  
    for i in range(len(a) - 1):
        if a[i: i + 2] == b[i: i + 2]:
            count += 1
    return count
