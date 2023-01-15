hello = "Hello World"
# print(hello)

name = "John"
origin = "Palu"

# Hello my name is John, from Palu
# print("Hello my name is " + name + ", from " + origin) # cara 1 (string concat)
# print("Hello my name is {}, from {}".format(name, origin)) # cara 2 (string formatting)
# print(f'Hello my name is {name}, from {origin}') # cara 3 (f string)

# print("Saya berjanji tidak akan mengulangi kenakalan saya")

# counter = 0
# while counter < 3: # condition
#     print(f'Sekarang nilai counter yaitu {counter}') # statement
#     # kalo nilai counter == 2, print "HELLO"
#     counter = counter + 1 # skrg nilai counter 1 # infinite loop

# print("end of program")

# people = ["John Doe", "Jane Doe", "Alex"] # list/ array
# for person in people:
#     print(person)

# fruits = ["Apple", "Orange", "Grapes"]
# for fruit in fruits:
#     print(f"Nama buah: {fruit}")

# for n in range(0, 7, 2): #[1, 2, 3, 4, .. ]
#    print(n)

# counter = 1
# while counter < 7:
#   print(counter)
#   counter += 2

# SOAL
# buat variable total dengan nilai 0. buat perulangan sebanyak 5 kali.
# setiap perulangan variable nilai total bertambah sebanyak 3.
# setelah perulangan berakhir, munculkan nilai total, maka akan tampil nilai 15.

# total = 0
# counter = 1 # 0, 1, 2, 3, 4
# while counter <= 5: # condition
#   total += 3 # statement
#   # print(total) # statement
#   counter += 1 # increment

# print(total)

counter = 0

# while counter < 100: # True/ False
#   print("Saya berjanji tidak akan mengulangi kenakalan saya")
#   counter += 1

# for i in range(100): # [0, 1, 2, .. , 99]
#   print("Saya berjanji tidak akan mengulangi kenakalan saya")
  
# copy line: alt + shift + down/up
# move line: alt + up/down
# delete line: alt + shift + K
# comment line: ctrl + /
# open terminal: ctrl + shift + `

# for i in range(1, 6): # 1, 2, 3, 4, 5
#   if i == 3:
#     continue # skip paksa perulangannya
#   print(i)

# syntax dasar penulisan function
# 1. dibuat
# 2. dipanggil
def add(first, second):
  result = first + second
  return result

def say_hello():
  return "say hello"

# def: keyword python utk buat function
# add: nama functionnya (bebas)
# argument/ parameter: hal-hal yang mau dipake (input)
# return: hal-hal yang mau dikeluarkan (output)

# name = "John" # global variable
def sapa():
  # name = "Jane" # local variable
  return "Hello" + name

# print(sapa())

# def kurang1(num1, num2):
#   return num1-num2

# def kurang2(num1, num2):
#   print(num1-num2)

# hasil = kurang1(5, 3)
# hasil2 = kurang2(5, 3)

# print(f'Hasil 1 = {hasil}')
# print(f'Hasil 2 = {hasil2}')

# Buatlah sebuah fungsi dengan nama “get_discounted_price”.
# Parameter fungsi adalah “base_price” dan “discount_percent”.
# base_price bertipe integer.
# discount_percent bertipe integer, merupakan persen diskon, angka dari 0 s/d 100.

# def get_discounted_price(base_price, discount_percent):
#   # misal base_price = 1000
#   # discount_percent = 20
#   # 800
#   return int(base_price - (base_price * (discount_percent * 0.01)))

# print(get_discounted_price(5000, 30))

# buat function: is_even
# punya 1 parameter 
# fungsinya untuk mengetahui apakah parameter yg diinput itu genap
# kalo genap, return 'True'
# kalo ganjil, return 'False'

# 2, 4, 6, 8, ... (genap) sisa bagi 2 == 0
# 1, 3, 5, 7, ... (ganjil) sisa bagi 2 != 0

def is_even(num):
  if (num % 2 == 0):
    return True
  return False