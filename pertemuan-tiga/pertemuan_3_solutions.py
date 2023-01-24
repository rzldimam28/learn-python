# --------------------------------------------------------------------------
# x = 3
# y = 5
# result = "Angka terbesar adalah "
# if x > y:
#   print(result + str(x))
# else:
#   print(result + str(y))

def max_of_two_sol1(num1, num2):
  result = "Angka terbesar adalah "
  if num1 > num2:
    return result + str(num1)
  else:
    return result + str(num2)

def max_of_two_sol2(num1, num2):
  result = "Angka terbesar adalah "
  if num1 > num2:
    return result + str(num1)
  return result + str(num2)

def max_of_two_sol3(num1, num2):
  result = "Angka terbesar adalah "
  return result + str(num1) if num1 > num2 else result + str(num2)

# --------------------------------------------------------------------------

def fizz_buzz_sol1(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return "None of the above"

def fizz_buzz_sol2(num):
  return "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else "None of the above"

# --------------------------------------------------------------------------

def fizz_buzz_list(arr):
  final_arr = []
  for num in arr:
    if num % 3 == 0 and num % 5 == 0:
      final_arr.append("FizzBuzz")
    elif num % 3 == 0:
      final_arr.append("Fizz")
    elif num % 5 == 0:
      final_arr.append("Buzz")
    else:
      final_arr.append("None of the above")
  return final_arr

# --------------------------------------------------------------------------

def sum_of_list(arr):
  total = 0
  for num in arr:
    total += num
  return total

# --------------------------------------------------------------------------

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def factorial_ternary(n):
  return 1 if n == 0 else n * factorial_ternary(n-1)

print(factorial_ternary(4))