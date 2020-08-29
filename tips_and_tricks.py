# Flag Method
def flag_method_for(nums):
    '''
    Using for loop
    The flag allows us to use a function or not to use it: continue, pass, etc.
    It helps if we want to skip certain numbers
    '''
    # Example exercise sum67
    counts = True # This is called a flag
    sum = 0
  
    for n in nums:
        if n == 6:
            counts = False
            continue
        if n == 7 and not counts:
            counts = True
            continue
        if counts:
            sum += n
    return sum

# Reading Frames
def reading_frames(str):
    '''
    How to search a string for another string
    How many times a string is within another one
    '''
    ctr = 0 # Create a counter
    compstr = str[len(str)-2 : len(str)] 
    # Stablish a var with wich we are going to compare the whole string
    # In this case we need the last two chars from the string
    # This is what we are going to check

    for i in range(len(str)-2): # Not taking the last two chars
        if str[i:i+2] == compstr: # Comparing them
            ctr += 1 # Adding to ctr if we find a match
    return ctr

# Better way of not using else:
def not_using_else(nums):
    for n in nums:
        if n == 1:
            return True
    return False

#   This is the same as
def using_else(nums):
    for n in nums:
        if n == 1:
            return True
        else: 
            return False

# Not for 2 variables
    # not(weekday == True and vacation == False)

# We need both cases, True or False
    # a == b 

# Create a var at the beginning of the function to add nums,chars, etc.
    # list(nums)
    # result = []
    # result = ''
    # list(chars)
    # d = {}

# len(str)+1,+2,+3,-1,-2,-3
    # [i:i+1] -- len(str)
    # [i:i+2] -- len(str)-1
    # [i:i+3] -- len(str)-2
    # [:i]    -- len(str)+1

# use range(60,81) instead of 60 < x < 80 

# Strings are not the same
def xyz_there(str):
    '''
    Return True if the given string contains an appearance of "xyz" where the xyz is not 
    directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    '''
    return str.count('xyz') - str.count('.xyz') > 0

def xyz_there2(str):
    '''
    Return True if the given string contains an appearance of "xyz" where the xyz is not 
    directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    '''
    return str.replace('xyz').find('.xyz') >= 0

def xyz_there3(str):
    '''
    Return True if the given string contains an appearance of "xyz" where the xyz is not 
    directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    '''
    for i in range(len(str)-2):
        if str[i:i+3] == 'xyz' and str[i-1] != '.':
            return True
    return False