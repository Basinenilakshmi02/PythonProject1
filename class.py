# class Person:
#      def __init__(self, name, age):
#      self.name=name
#      self.age=age
#      def display(self):
#        print(f"Name: {self.name},age: {self.age}")
# name =  input("Enter your name:")
# age = int(input("Enter age:"))
#person = Person(name,age)
#person.display()



# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2 * (self.length + self.width)
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# rectangle = Rectangle(length, width)
# print(f"Area:{rectangle.area()}")
# print(f"Perimeter:{rectangle.perimeter()}")


# fruits_list = ("banana", "mango", "apple", "watermelon")
# fruits_list = list(fruits_list)
# fruits_list.append("papaya")
# print(fruits_list)

# x=10
# y=20
# print(x+y)
# num1 = 30
# num2 = 40
# print(num1+num2)
# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# print(f"sum of two numbers is: {x+y}")
# def reversed_list(list):
#     return list[::-1]
# # fruits = ["banana","mango","papaya","apple"]
# reversed_fruits = fruits[::-1]
# print(reversed_fruits)
# a = 2
# if (a % 2 == 0):
#     print("Even")
# else:
#     print("odd")
# age = 18
# weight = 57
# if age >= 18:
#     if weight >= 50:
#         print("eligible")
#     else:
#         print("no eligible")
# else:
#     print("Not eligible")
# ch=input("enter a character: ")
# if ch.isupper():
#     print("uppercase")
# elif ch.islower():
#     print("lowercase")
# else:
#     print("no character")
#
# def find_middle_digit(num):
#     number_str = str(num)
#     length = len(number_str)
#     if length % 2 == 1:
#         middle_index = length // 2
#         print(f"The middle digit is: {number_str[middle_index]}")
#     else:
#         print("The number has even no. of digits,so it has no single middle digit")
# num = int(input("Enter a number: "))
# find_middle_digit(num)

# def find_armstrong_number(number):
#     number_str = str(number)
#     num_digits = len(number_str)
#     total = 0
#     for digit in number_str:
#         total += int(digit)**num_digits
#     if total == number:
#         print("armstrong number")
#     else:
#         print("not a armstrong number")
# number = int(input("Enter a number: "))
# print(find_armstrong_number(number))
# def is_palindrome(word):
#     return word == word[::-1]
# word = "malayalam"
# print(is_palindrome(word))
# number = "121"
# reversed_number = number[::-1]
# if reversed_number == number:
#     print("palindrome")
# else:
#     print("not a palindrome")
# text = "venu gopal"
# char = {}
# for c in text:
#     if c in char:
#         char[c]+=1
#     else:
#         char[c]=1
# print(char)
# x,y=10,50
# x,y=y,x
# print("x:", x)
# print("y:", y)

# x,y=5,7
# print("Before swapping:",x,y)
# x,y=y,x
# print("After swapping:",x,y)

# def sum_of_natural_numbers(N):
#     total = 0
#     count=1
#     while count <= N:
#         total += count
#         count += 1
#     return total
# N=11
# result = sum_of_natural_numbers(11)
# print("The sum of the first",N,"Natural numbers is:",result)

# num = 5
# res = 0
# for i in range(1, num+1):
#     res += i ** 3
# print(res)
# n=int(input("Enter a number: "))
# res=0
# for i in range(1, n+1):
#     res += i**2
# print(res)
# def sum_of_squares(n):
#     res=0
#     for i in range(1,n+1):
#         res += i**2
#     return res
# n=5
# result = sum_of_squares(5)
# print("sum of squares is:",result)
# def multiplication_table(n):
#     for i in range(1,11):
#         print(i*n)
# multiplication_table(3)
# num=int(input("Enter a number: "))
# total=0
# for i in range(1,11):
#     total += i*2
# print(total)


# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num, "x", i, "=", num*i)
# def StringJumper(str):
#     for i in range(0, len(str), 2):
#         print(str[i],end=" ")
# StringJumper("doctorphenomenal")
# s = "lakshmi"
# print("Hello " + s)
# a = "Yuvasri"
# print("hi " + a)
# a=10
# b=20
# result=str(a) + str(b)
# print(result)
# a="Hello"
# b="world"
# print(a + " " + b)
# n = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# count = 0
# if n<=0:
#     print("please enter a positive number")
# elif n==1:
#     print("Fibonacci sequence")
#     print(a)
# else:
#     print("Fibonacci sequence")
#     while count<n:
#         print(a,end=" ")
#         c = a + b
#         a = b
#         b = c
#         count+=1
# s="    codegnan is a institute     "
# print(s.strip())
# s="hello"
# print(s.center(10))
# print(s.center(20,"*"))
# n=int(input("Enter number of terms: "))
# a=0
# b=1
# count=0
# while count<n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     count+=1
# s="codegnan"
# print(s.index("n"))
# s="codegnan"
# print(s.rfind("n"))
# print(s.find("z"))
# print(len(s))
# l=[1,2,3,4]
# print(l)
# l=[1,2,3,4]
# print(l)
# l.append(5)
# print(l)
# l=[1,2,3,4,5]
# l.extend([6,7])
# # print(l)
# l=[2,3,4,5,6,7,8]
# l.remove(2)
# print(l)
# l.pop()
# print(l)
# l=[1,2,3,4,5,6,6]
# del l[1]
# print(l)
# t=(1,2,3,4,5,6,7,8)
# print(min(t))
# print(max(t))
# print(sum(t))
# print(len(t))
# print(t.index(5))
# print(t.count(1))
# print(t.index(3))
# person = {"name":"raju","age":23,"village":"hyderabad"}
# print(person)
# print(person["name"])
# print(person["age"])
# person["name"]="rani"
# print(person["name"])
# s={10,1,14,2,4}
# print(type(s))
# print(s)
# s.add(19)
# print(s)
# s.remove(10)
# print(s)
# s.update({16,17,23})
# print(s)
# a={1,2,3}
# b={3,4,5}
# print(a.union(b))
# print(a|b)
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a^b)
# print(a.issubset(b))
# print(a.issuperset(b))
# numbers = [1,2,3,4,5,6,7,8,9,10]
# sum=0
# for num in numbers:
#     sum += num
# print("sum of all elements:",sum)
# my_list=[1,2,3,4,5,6,7,8,9,10]
# alternate_numbers = my_list[::-2]
# print("Alternate numbers:",alternate_numbers)
# sum_of_alternate = alternate_numbers
# # print("sum of alternate numbers:",sum_of_alternate)
# import math
# def is_perfect_square(num):
#     if num < 0:
#         return False
# #     root = int(math.sqrt(num))//
# def is_perfect(number):
#     if number <= 0:
#         return False
#     sum_divisors = 0
#     for i in range(1, number):
#         if number % i==0:
#             sum_divisors += i
#     return sum_divisors == number
# try:
#     num = int(input("Enter a number: "))
#     if is_perfect(num):
#         print(f"{num} is a perfect number")
#     else:
#         print(f"{num} is not a perfect number")
# except ValueError:
#      print("please enter a valid integer")
# num = int(input("Enter a number: "))
# if num > 1:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#         if is_prime:
#             print(num,"is a prime number")
#         else:
#             print(num,"is not a prime number")
#     else:
#         print(num,"is not a prime number")





























