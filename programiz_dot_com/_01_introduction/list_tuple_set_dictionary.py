# List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].

# Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

# Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }. 

#--------------------     . LIST

languages = ["Swift", "Java", "Python"]

# access element at index 0
print(languages[0])   # Swift

# access element at index 2
print(languages[2])   # Python

#--------------------     . TUPLE
# create a tuple 
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0])   # Microsoft

# access element at index 1
print(product[1])   # Xbox

#--------------------     . SET

# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))

#--------------------     . DICTIONARY

# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city['Nepal'])  # prints Kathmandu

# print(capital_city['Kathmandu'])  # throws error message 