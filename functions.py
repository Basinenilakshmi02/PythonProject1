#a=-10
#rint(abs(a))
#print(a)
#def greet():
  ## greet()
##greet()
#def fact(n):
   # if n==0 or n==1:
    #    return 1
  ##  else:
       # return n * fact(n-1)
#print(fact(5))
#a=0
#b=1
#print(a,b, end=" ")
#for i in range(11):
 #   sum=a+b
 #   print(sum,end=" ")
 #   a=b
  ##  b=sum
#x=lambda a,b:a+b
#print(x(10, 20))
#x=lambda a,b:a+b
#c=x(10,20)
#print(c)
#def check_neon(num):
   # squared = num ** 2
    #digit_sum = 0
    #while squared > 0:
  #      digit_sum += squared % 10
   #     squared //= 10
 #   return digit_sum == num
#num=int(input("Enter a number:"))
#if check_neon(num):
 #       print(f"{num} is a neon number.")
#else:
 #       print(f"{num} is not a neon number")

#check_neon(n)
#def check_automorphic(num):
  #   return str(squared).endswith(str(num))
#n=int(input("Enter a number:"))
#if check_automorphic(n):
 #   print(f"{n} is an Automorphic number.")
#else:
   # print(f"{n} is not a Automorphic number.")

import math

def is_strong_number(num):
    original = num
    total = 0

    #while num > 0:
      #  digit = num % 10
     #   total += math.factorial(digit)
    #    num //= 10
   # return total == original

# Example usage
#n = int(input("Enter a number: "))
#if is_strong_number(n):
 #   print(f"{n} is a Strong number.")
#else:
  #  print(f"{n} is not a Strong number.")
#l=[10,20,30,50,40]
#new_list =list(map(lambda a:a+10, l))
#print(new_list)
from functools import reduce
#l=[1,2,3,4,5,]
#result=reduce(lambda a,b:a+b,l)
#print(result)
#a=6
#print(bin(a))
#++++number = int(input("Enter a number: "))
#binary = bin(number)[::2]
#print(f"Binary representation of {number} is {binary}")

#a=106
#print(chr(a))

#ch="C"
#print(ord(ch))
#numbers=[1,2,3,1,2,5,4]
#frequency={}
#for num in numbers:
    #if num in frequency:
   #     frequency[num] += 1
  #  else:
 #       frequency[num] = 1
#for num, count in frequency.items():
#    print(f"{num}: {count}")
#n=[1, 2, 3, 4, 5, 6]
#even = filter(lambda x: x%2==0, n)
#print(list(even))
#x="2"
#y=3
#print(x*y)











