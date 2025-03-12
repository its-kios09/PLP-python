#Understanding the python data type
#data types specify the type of data that can be stored inside a variable.
# Everything is an object in Python programming, data types are actually classes and variables are instances(object) of these classes.

num1 = 5
print(num1, 'type of ', type(num1))
num1 = 5.2
print(num1, 'type of ', type(num1))
num1 = 5.23322
print(num1, 'type of ', type(num1))

langauge = ['Swift', 'Java', 'Python']
print(langauge)
# we access the element from the list data type by indexing
print(langauge[1])
# A tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
typesOfLeadership = ('President', 'Minister', 'Governor')
print(typesOfLeadership, 'type of ', type(typesOfLeadership))

# Python dictionary is an ordered collection of items. It stores elements in key/value pairs.
capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city, 'type of ', type(capital_city))

# Python Set Data Type
typesOfGender = {'Male', 'Female', 'Other'}
print(typesOfGender, 'type of ' ,type(typesOfGender))