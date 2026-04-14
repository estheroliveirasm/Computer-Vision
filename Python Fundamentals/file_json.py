# What is a JSON (it is a dictionary)
import json

# Reading a file
with open('numpy.py', 'r') as file:
    print(file.read())

# Saving files
s = "You are reading my credit card password"
with open('password.txt', 'w') as file:
    file.write(s)

d = { 
    'first_name': 'Esther',
    'age': 19,
    'last_name': 'Oliveira'
}

# Saving a JSON
with open('data.json', 'w') as file:
    json.dump(d, file)

# Loading a JSON
with open('data.json', 'r') as file:
    print(json.load(file))