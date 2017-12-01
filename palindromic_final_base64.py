'''
Find the first 1000 positive decimal integers (n) are palindromes and the asscoiated smallest base (b).
E.g. (1,2), (2,3), (3,2), (4,3), ...
This python scripy is using base 2 until base 32
'''
import sys

try:
   numpali = int(raw_input('How many positive palindrome numbers do you want to find?  '))
   if numpali < 0:
       print("That's negative!")
       sys.exit()
except ValueError:
   print("That's not an integer!")
   sys.exit()

count=0

def convert_base(number, base):
    ''' Convert number to base 2 until 64 '''
    base_string = '0123456789ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghigklmnopqrstuvwxyz+/'
    if number < base:
        return base_string[number]
    else:
        return ''.join((convert_base(number//base, base),
                        base_string[number % base]))

def palindrome(value):
    ''' Evaluates a String, returning if it is palindrome or not '''
    return value.upper() == (value[::-1]).upper()

def minimal_palindrome_base(number):
    ''' Find the smallest base for a given number and increment the number'''
    if count < int(numpali)+1:
       for base in range(2,65):
          if palindrome(convert_base(number, base)):
             return base
       return -1

if __name__ == '__main__':
    number =1
    while count < int(numpali):
        minimal_palindrome = minimal_palindrome_base(number)
        if(minimal_palindrome !=-1):
           base = minimal_palindrome
           print ('The first ' + str(count+1) +' positive palindrome number is {n} for the minimal base {b} (up to base 64)'.format(n=number, b=base))
           number +=1
           count +=1
        else:
           number +=1
