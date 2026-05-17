# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

                                                        #Exercises: Level 1
#Find the length of the set it_companies
print(f"The length of the set it_companies is : {len(it_companies)}")

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Safecode','Codeforce','Naval'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Codeforce')
print(it_companies)

#What is the difference between remove and discard (Ans : discard keeps the order as it was before)
it_companies.discard('Safecode')
print(it_companies)


                                                        #Exercises: Level 2
#Join A and B
print("Set A = ", A)
print("Set B = ",B)

C = A.union(B)
print("Set C = ", C)

#Find A intersection B
intset = A.intersection(B)
print("A intersection B = ", intset)

#Is A subset of B
print(f"Is A subset of B?  = {A.issubset(B)}")

#Are A and B disjoint sets
print(f"Are A and B disjoint sets?  = {A.isdisjoint(B)}")

#Join A with B and B with A
AB = A.union(B)
print(AB)
BA = B.union(A)
print(BA)

#What is the symmetric difference between A and B
print(f"The symmetric difference between A and B = {A.symmetric_difference(B)} ")

# Delete the sets completely
del A

                                                            # Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
st_age = set (age)
print(st_age)

sentence =  "I am a teacher and I love to inspire and teach people." 

#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

lt_word = sentence.split()
unique_words = set (lt_word)
print(unique_words)
print(f"How many unique words have been used in the sentence? = {len(unique_words)}")