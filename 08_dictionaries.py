#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Minix'
dog['color'] = 'White'
dog['legs'] = 4
dog['age'] = 4

print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Asha', 'last_name': 'Moni', 'gender': 'Female', 'age':25, 'marital_status': 'Unmarried', 'skills':['Python', 'Java'], 'country': 'Dhaka', 'city':'Dhaka', 'address':'Cantonment'}

#Get the length of the student dictionary
print(f"The length of the student dictionary is: {len(student)}")

#Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

#Modify the skills values by adding one or two skills
student['skills'].append('C++')
print(student)

#Get the dictionary keys as a list
keys_list = student.keys()
print(keys_list)

#Get the dictionary values as a list
keys_values = student.values()
print(keys_values)

#Change the dictionary to a list of tuples using items() method
print(student.items())

#Delete one of the items in the dictionary
student.pop('city')
print(student)

#Delete one of the dictionaries
del dog