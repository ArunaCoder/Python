# https://stackabuse.com/check-if-string-contains-a-number-in-python/

# The isnumeric() function returns True if the input string contains only numbers, otherwise, it returns False:

# str1 = '918'
# print('String is whole numeric?', str1.isnumeric()) #True

# str3 = '-918'
# print('String is whole numeric?', str1.isnumeric()) #True

# str4 = '9.18'
# print('String is whole numeric?', str1.isnumeric()) #True

# str2 = 'The meaning of the universe is 42'
# print('String is whole numeric?', str2.isnumeric()) #False

input_string = "My name is Satyam & I am 20 yrs old"
flag = False
for ch in input_string:
    if ch.isnumeric():
        flag = True
        break
if flag:
    print("Yes, the string contains a number.")
else:
    print("No, the string does not contain a number.")