l=[i+2 for i in range(1,6) if(i%2==0)]
print(l)
l=[i**2 for i in range(1,11)]
print(l)


l=["jam","apple",",mango"]
k=[i.upper() for i in l]
print(k)
price=[900,400,500,300]
k=[i for i in price if()]
print(k)
product_details=[("laptop",5000),("mobile",6000),("watch",15000)]
l=[item for item,price in product_details if price>5000]
print(l)
l=[1,2,3,4]
k=[i for i,j in enumerate(l) if j%2==0]
print(k)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def factors.append(i)
           n = n//i
        else:
            i += 1
    return factors
def is_smith(num):
    if is_prime(num):
       return False
    return digit_sum(num) == sum(digit_sum(f) for f in prime_factors(num))
num = int(input("Enter a number: "))
if is_smith(num):
    print(num,"is a Smith number")
else:
    print(num,"is not a Smith number")
def sqrt_integer(n):
     if n < 0:
         return "Square root not defined for negative numbers."
     if n == 0 or n == 1:
         return n
     low = 0
     high = n
     ans = 0
     while low <= high:
         mid = (low + high) // 2
         if mid * mid == n:
             return mid
         elif mid * mid < n:
             ans = mid
             low = mid + 1
         else:
             high = mid - 1
     return ans
num=36
print("Square root of",(num),"is",sqrt_integer(num))
def find_middle_digit(number):
    num_str = str(number)
    length = len(num_str)
    f length % 2 == 1:
        middle_index = length // 2
       print(f"The middle digit is:{num_str[middle_index]}")
    else:
        print("the number has  even number of digits,so it has no single middle digit")
num=int(input("Enter a number: "))
find_middle_digit(num)
def find_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total=0
    for digit in num_str:
        total += int(digit)**num_digits
    if total == number:
        return True
    else:
        return False
um=int(input("Enter a number:"))
print(find_armstrong_number(num))
def print_duplicate_characters(s):
    char_count = {}
    duplicates = set()
    for char in s:
        if char in char_count:
            char_count[char] += 1
            duplicates.add(char)
        else:
            char_count[char] = 1
    if duplicates:
        print("Duplicate characters are:")
        for char in sorted(duplicates):
            print(f"'{char}'{char_count[char]} times")
    else:
        print("No duplicates are found")
string_input=input("Enter a string: ")
print(print_duplicate_characters(string_input))
char = {}
for c in "Hello":
    if c in char:
        char[c] += 1
    else:
        char[c] = 1
print(char)
string=input("enter a string: ")
















