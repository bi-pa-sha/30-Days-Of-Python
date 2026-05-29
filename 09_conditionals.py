#90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F


try:
    mark = int(input("Enter Your Mark: "))

    if 90<=mark<=100:
        print("You got A")
    elif 80<=mark<=89:
        print("You got B")
    elif 70<=mark<=79:
        print("You got C")
    elif 60<=mark<=69:
        print("You got D")
    elif 0<=mark<=59:
        print("You got F")
    else:
        print("You have entered invalid number")

except:
    print("Invalid Number")



#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer

month = input("Enter month: ")
Summer = ['June', 'July', 'August']
Spring = ['March', 'April', 'May']
Winter = ['December', 'January', 'February']
Autumn = ['September', 'October', 'November']

if any(s.lower() == month.lower() for s    in Summer):
    print("The season is Summer")
elif any(sp.lower() == month.lower() for sp   in Spring):
    print("The season is Spring")
elif any(w.lower() == month.lower() for w   in Winter):
    print("The season is Winter")
elif any(a.lower() == month.lower() for a   in Autumn):
    print("The season is Autumn")
else:
    print("Invalid month")




#fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')


fruits = ['banana', 'orange', 'mango', 'lemon']
f = input("Enter a Fruit: ")

if any(fruit.lower() == f.lower() for fruit in fruits):
    print('That fruit already exist in the list')
else:
    fruits.append(f)
    print(fruits)
    

# Exercises: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
n = len(person["skills"])
print(n)
if 'skills' in person:

 # Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
    skills = person['skills']
    n = len(skills)
    if n % 2 == 0:
        print("The middle skill in the skills list is:", skills[n//2 - 1], skills[n//2])
    else:
        print("The middle skill in the skills list is:", skills[n//2])


 # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    if 'Python' in skills:
        print("Person has python skill")
    else:
        print("Person has no python skill")


 # If a person skills has only JavaScript and React, print('He is a front end developer'), 
 # if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 # else print('unknown title') - for more accurate results more conditions can be nested!

    skills = set(person['skills'])
    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('He is a fullstack developer')
    else:
        print('Unknown title')
else:
    print("person has no skills key!")

# If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] and person['country'] == 'Finland':
    print("Asabeneh Yetayeh lives in Finland. He is married.")
else:
    print("false Information")