import math
import string
from functools import partial
from functools import reduce
import itertools

def fibonacci(n,cache={}): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    elif n in cache:
        return cache[n]
    else: 
        result = fibonacci(n-1)+fibonacci(n-2)
        cache[n] = result
        return result

fibonacci_series = [fibonacci(x) for x in range(10000)]

def check_fibonacci(n):
    '''
    Inputs:
        n: number to be checked
    Returns:
        True when n is a fibonacci number else False
    '''
    check = list(filter(lambda x: x==n,fibonacci_series))
    if check:
        return True
    else:
        return False

def add_two_iterables(a,b):
    '''
    Inputs:
        a: Iterable which has to be even
        b: Iterable which has to be odd
    Output:
        List which adds a,b elements is a is even, b is odd
    '''
    return [x+y for x,y in zip(a,b) if x%2==0 and y%2==1]

def strip_vowels_from_string(word):
    '''
    strips every vowel from a string provided (tsai>>t s)
    '''
    vowels = ['a','e','i','o','u']
    return ''.join([x for x in word.lower() if x not in vowels])

def relu(array_1d):
    '''
    acts like a ReLU function for a 1D array
    '''
    return [max(x,0.0) for x in array_1d]

def sigmoid(array_1d):
    '''
    acts like a sigmoid function for a 1D array
    '''
    return [1.0/(1.0+math.exp(-x)) for x in array_1d]

def shift_by_5(ch):
    '''
    shift character by 5
    '''
    val = ord(ch)  
    # if k-th ahead character exceed 'z'  
    if val > 117:  
        ch_new = chr(val - 117+96)  
    else:  
        ch_new = chr(val + 5)
    return ch_new

def shift_word_by_5(word):
    '''
    takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
    '''
    return ''.join([shift_by_5(x) for x in word.lower()])


def reduce_even_nums(a):
    '''
    add only even numbers in a list
    '''
    return reduce(lambda x,y: x+y, filter(lambda x : x%2==0,a))

def reduce_biggest_char(a):
    '''
    find the biggest character in a string (printable ascii characters)
    '''
    return reduce(lambda x,y: x if ord(x) > ord(y) else y, a)

def reduce_add_3rd_num(a):
    '''
    adds every 3rd number in a list
    '''
    return reduce(lambda x,y: x+y, a[::3])

def generate_15_random_num_plates():
    '''
    expression that generates 15 random KADDAADDDD number plates
    '''
    return ['KA'+str(random.randint(10,99))+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+str(random.randint(1000,9999)) for _ in range(15)]


def generate_num_plate(num_range,state_initial):
    return state_initial+str(random.randint(10,99))+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+str(num_range)

partial_func_1500 = partial(generate_num_plate,1500)





