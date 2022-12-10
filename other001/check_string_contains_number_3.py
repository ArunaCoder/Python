# https://stackabuse.com/check-if-string-contains-a-number-in-python/

# The isdigit() function checks whether all the characters in a string are digits. If yes - it returns True, and if not, it returns False

input_string = "My name is Silva and I am 44 yrs old"
flag = False
for ch in input_string:
    if ch.isdigit():
        flag = True
        break
if flag:
    print('1','Yes, the string contains a number.')
else:
    print('1','No, the string does not contain a number.')

number_1 = '0.5'

print('2',number_1.isdigit())
print('3',number_1.isdecimal())

s = "28212"
print('4',s.isdecimal())

# contains alphabets
s = "32ladk3"
print('5',s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print('6',s.isdecimal())
