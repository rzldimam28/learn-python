# buat variabel
# x = 92
# y = 3

# # buat algoritma
# if x > y:
#   print("Angka terbesar adalah " + str(x))
# else:
#   print("Angka terbesar adalah " + str(y))

def max_of_two_numbers(x, y): # sebuah function hanya bisa me return sebuah nilai
  if x > y:
    return "Angka terbesar adalah " + str(x) 
  else:
    return "Angka terbesar adalah " + str(y)

def max_of_two_numbers_2(x, y):
  if x > y:
    return "Angka terbesar adalah " + str(x)  
  return "Angka terbesar adalah " + str(y)

# ternary operator
def max_of_two_numbers_3(x, y):
  return "Angka terbesar adalah " + str(x) if x > y else "Angka terbesar adalah " + str(y)

#fizz_buzz

def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 5 == 0:
    return "Buzz"
  elif num % 3 == 0:
    return "Fizz" 
  else:
    return "None of the above"

hasil = fizz_buzz(10)
print(hasil)

my_list = [5, 7, 19, 25, 30]

def fizz_buzz_list(arr): #array (list)
  result = []
  for angka in arr:
    if angka % 3 == 0 and angka % 5 == 0:
      result.append("FizzBuzz")
    elif angka % 5 == 0:
      result.append("Buzz")
    elif angka % 3 == 0:
      result.append("Fizz")
    else:
      result.append("None")
  return result

def sum(arr):
  hasil = 0
  for i in arr:
    hasil += i
  return hasil

coba = sum([1, 2, 4, 3, 8])
print(coba)

# macam2 inisiasi
list_kosong = []
angka = 0
string_kosong = ""
dict_kosong = {}

def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num-1)

c = factorial(4)
print(c)

# 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# fac