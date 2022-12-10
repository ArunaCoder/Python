# https://stackabuse.com/check-if-string-contains-a-number-in-python/

# The ord() function takes a character and returns its ASCII value:

# print(ord('0'))
# print(ord('9'))

input_string = "My name is Silva and I am 44 yrs old"
flag = False
for ch in input_string:
    ascii_code = ord(ch)
    if 47 < ascii_code < 58:
        flag = True
        break
if flag:
    print('Yes, the string contains a number.')
else:
    print('No, the string does not contain a number.')