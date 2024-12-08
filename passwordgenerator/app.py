import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


biglist_list_letters = random.sample(letters,nr_letters)
list_symbols = random.sample(symbols,nr_symbols)
for sy in list_symbols:
    biglist_list_letters.append(sy)
list_numbers = random.sample(numbers,nr_numbers)
for num in list_numbers:
    biglist_list_letters.append(num)

nr_total = nr_symbols + nr_letters + nr_numbers
temp_list = random.sample(biglist_list_letters,nr_total)

result = ""
for pw in temp_list:
    result += str(pw)
print(f"Your password is {result}.")




