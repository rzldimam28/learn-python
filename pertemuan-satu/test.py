name = "Andri Batewa" # string (kata-kata)
num_of_participant = 5 # integer (bil bulat)
weights = 40.5 # float (bil desimal)
is_male = True # bool
is_rainy = False # bool
x = None # None

list_participant = ["imam", "ade", "chalfin", "anggun", "ayu"] # list
# indexing (dimulai dari 0)
# slicing (mengambil bbrp elemen)
# print(list_participant[1:4]) # ambil index dari 0 sampe 2-1 (1)

contoh_tuple = ("ka tahzan", "ka masnur", "pak iman") # tuple

# dict (dictionary)
# terdiri dari satu atau lebih key-value
person = {
  "name": "John",
  "age": 20,
  "is_married": True,
}
# print(person["name"])

# comparison operator
# print("Imam" != "imam")
# print("Imam" > "imam") # pr
# print(12 < 6)

# arithmetic operator
# print(1 + 3)
# print(10 - 5)
# print(10 - 11)
# print(2 * 3)
# print(20 / 10)
# print(5 % 2) # modulus (sisa bagi) = 1

# logical operator
# print(not True and False or not True)

# string concat (penggabungan)
# first_name = "imam"
# last_name = "rizaldi"
# print(first_name + " " + last_name)

first_abc = "a"
greetings = "Hello, I'm John"
last_abc = 'z'
# print(first_abc, last_abc)

# control flow (if)
is_married = True
if is_married == False:
  print("cepat2 sudah kawin")

score = 100
treshold = 90

# blocking dan indentasi

toppings = 'rambutan'

if toppings == 'vanilla':
  print('Vanilla toppings added!')
elif toppings == 'chocolate':
  print('Chocolate toppings added!')
elif toppings == 'strawberry':
  print('Strawberry toppings added!')
else:
  print('No toppings')
