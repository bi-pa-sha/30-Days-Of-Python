                                                                      # Exercises: Level 1

#Create an empty tuple
empty_tpl = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters_tpl = ('Zini','Mini','Zehu')
brothers_tpl =('zendo','mondo','bindo')

#Join brothers and sisters tuples and assign it to siblings
siblings_tpl = brothers_tpl + sisters_tpl
print(siblings_tpl)

#How many siblings do you have?
print(f"I have {len(siblings_tpl)} siblings")


#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings_lt = list(siblings_tpl)

father_name = 'Mickanzi'
motther_name = 'Noumi'

siblings_lt.append(father_name)
siblings_lt.append(motther_name)

family_members = tuple (siblings_lt)
print(family_members)





                                                                        #Exercises: Level 2
#Unpack siblings and parents from family_members
siblings = family_members[0:6]
print(siblings)
parents = family_members[6:]
print(parents)


#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits =('apple','mango','orange')
vegetables =('potatoes', 'tomatoes', 'onions', 'carrots', 'broccoli')
animal_products =('milk', 'meat', 'beef', 'chicken', 'mutton', 'cheese', 'butter', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_lt)//2
print(food_stuff_lt[middle -1])

# Slice out the first three items and the last three items from food_stuff_lt list
first_food_stuff_lt = food_stuff_lt[0:3]
print(first_food_stuff_lt)
last_food_stuff_lt = food_stuff_lt[-3:]
print(last_food_stuff_lt)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp


#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Denmark' in nordic_countries:
    print("item exists in tuple")

#Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print("'Iceland' is a nordic country")
