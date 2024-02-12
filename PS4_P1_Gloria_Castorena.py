'''
Name: <Gloria Castorena>
Student ID: 1221643982
Course: IFT 101
Priblem Set: PS4
Problem: P1
Date:<02-02-2024>
'''
#create list
dogs = ["Bulldog", "Poodle", "Beagle", "Terrier"]
#print list
print("List:", dogs)
# convert list to dogs_tuple
dogs_tuple = tuple(dogs)
# print the tuple
print("Tuple:", dogs_tuple)
#convert dog list into dogs_set
dogs_set = set(dogs)
#print set
print("Set:", dogs_set)
#convert the dogs list to a dictionary named dogs_dict
dogs_dict = {dog: len(dog) for dog in dogs}
#print the dictionary
print("Dictionary:", dogs_dict)
#add "Pug" and "Chihuahua" to the list
dogs.extend(["Pug", "Chihuahua"])
#Remove "Beaagle" from dogs list
dogs.remove("Beagle")
#Print updated list
print("Updated list:", dogs)
#update dogs_dict to reflect changes made to dogs list
dogs_dict = {dog: len(dog) for dog in dogs}
#print updated dictionary
print("Updated dictionary:", dogs_dict)

