# --------factorial----------#

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(3))

# --------fibonacci using recursion -----------#
n=4

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print('fibonacci',n,fibonacci(3))

# ----printing fibonacci series upto n  using recursion --------#
def print_fibonacci(n,c=1):
    if c > n:
        return
    print(fibonacci(c),end=' ')
    return print_fibonacci(n,c+1 )
print_fibonacci(4)

# ----printing fibonacci series upto n  using iteration and finding sum of series of number --------#

a=0
for i in range(n):
    print(fibonacci(i),end=' ')
    a += fibonacci(i)
print()
print('sum of fibonacci',a)

#  ----string reversing ------#

s='subahana'
print(s,s[:-1],s[1:-1])
def reverse_string(s):
    if len(s) <= 0:
        return ''
    # print(s[-1] + reverse_string(s[:-1]))
    return s[-1] + reverse_string(s[:-1])
print(reverse_string(s))
# reverse_string(s)

# ----checking palindrome------#

def check_pali(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return check_pali(s[1:-1])
print(check_pali('malayalam'))
print(check_pali(s))


# ------Count the Occurrences of a Character in a String----#

def count_char(s,char):
    if len(s) == 0:
        return 0
    return (1 if s[0] == char else 0) + count_char(s[1:],char)

print(count_char(s,'a'))

# -----Remove All Occurrences of a Character-----#

def remove_char(s,char):
    if len(s)== 0:
        return ''
    return ('' if s[0] == char else s[0]) + remove_char(s[1:],char)
print(remove_char(s,'a'))

#--------binary_search---------#

def binary_search(target,arr,left,right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > left:
        return binary_search(target,arr,left,mid - 1)
    else:
        return binary_search(target,arr,mid + 1,right)

arr=[0,1,2,3,4,5,6,7,8]
target=0
print(binary_search(target,arr,0,len(arr)-1))

# ------finding digit sum ----#

def digit_sum(n):
    if n == 0:
        return n
    return n % 10 +digit_sum(n//10)
print(digit_sum(2))
def digit_sum_str(n):
    n=str(n)
    if n == '':
        return 0
    return int(n[0]) + digit_sum_str(n[1:])
print(digit_sum_str(2))
x=[1,2,3]
print(x[::-1])