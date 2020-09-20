# cigar_party
def cigar_party(cigars, is_weekend):
    '''
    When squirrels get together for a party, they like to have cigars. A squirrel party
    is successful when the number of cigars is between 40 and 60, inclusive. Unless it
    is the weekend, in which case there is no upper bound on the number of cigars.
    Return True if the party with the given values is successful, or False otherwise.
    '''
    if is_weekend:
        return cigars >= 40
    return cigars in range(40,61)

# date_fashion
def date_fashion(you, date):
    '''
    You and your date are trying to get a table at a restaurant. The parameter "you"
    is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness
    of your date's clothes. The result getting the table is encoded as an int value with
    0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes).
    With the exception that if either of you has style of 2 or less, then the result is 0 (no).
    Otherwise the result is 1 (maybe).
    '''
    if you <= 2 or date <= 2:
        return 0
    if you > 7 or date > 7:
        return 2
    return 1

# squirrel_play
def squirrel_play(temp, is_summer):
    '''
    The squirrels in Palo Alto spend most of the day playing. In particular, they play if the
    temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is
    100 instead of 90. Given an int temperature and a boolean is_summer, return True if the
    squirrels play and False otherwise.
    '''
    if is_summer:
        return temp in range(60,101)
    return temp in range(60,91)

# caught_speeding
def caught_speeding(speed, is_birthday):
    '''
    You are driving a little too fast, and a police officer stops you. Write code to compute
    the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed
    is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your
    speed can be 5 higher in all cases.
    '''
    speeding = speed - (65 if is_birthday else 60)

    if speeding > 20:
        return 2
    elif speeding > 0:
        return 1
    else:
        return 0

# sorta_sum
def sorta_sum(a, b):
    '''
    Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive,
    are forbidden, so in that case just return 20.
    '''
    if a+b in range(10,20):
        return 20
    return a+b

# alarm_clock
def alarm_clock(day, vacation):
    '''
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating
    if we are on vacation, return a string of the form "7:00" indicating when the alarm clock
    should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should
    be "off".
    '''

  early = '7:00' if not vacation else '10:00'
  late = '10:00' if not vacation else 'off'

  return early if day in range(1,6) else late

#love6
def love6(a, b):
    '''
    The number 6 is a truly great number. Given two int values, a and b, return True if either one
    is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute
    value of a number.
    '''
  return a+b == 6 or a == 6 or b == 6 or abs(a-b) == 6

# in1to10
def in1to10(n, outside_mode):
    '''
    Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True,
    in which case return True if the number is less or equal to 1, or greater or equal to 10.
    '''
    if outside_mode:
        return n not in range(2,10)
    return n in range(1,11)

# near_ten
def near_ten(num):
    '''
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
    Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
    '''
    nums = [num+2, num+1, num, num-1, num-2]

    for n in nums:
        if n % 10 == 0:
            return True
    return False
