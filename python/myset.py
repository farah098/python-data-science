# Python set we use {}
# Set does not allow duplicates
# Set is not ordered (items does not retain its position)
# Set is not index (do not have indexes like 0,1,2,3,4....)
# Set is modifiable
fruits = {"apple","orange","mango","apple","banana", "grapes", "apple"}
print(fruits)

# Selection and Indexing
# You cannot select the item using Index
# But you can always iterate using for loop
# print(fruits[0])

for fruit in fruits:
    print(fruits)

# Modifiable 
fruits.add("durian")
print(fruits)

# Update
# fruits[2] = "rambutan"
# If you want to update drop the old fruit and add the new fruit

# Drop a fruit
# fruits is an object or instance of a set class
# remove is a method inside the object fruits
fruits.remove("grapes")
print(fruits)

# you can also use pop
# however pop will randomly "remove an item"
fruits.pop()
print(fruits)

# NLP => Natural Language Processing
# NLTK 

overseafruits = {"apple","orange","mango","banana", "grapes"}
localfruits = {"durian","rambutan","cempedak","mangosteen", "banana"}

print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))

favoritefruits ={"durian","rambutan","mangosteen"}
print(favoritefruits.issubset(localfruits))
print(localfruits.issuperset(favoritefruits))
print(favoritefruits.isdisjoint(overseafruits))

listfruits = list(fruits)
listfruits.clear()
print(listfruits) # empty list

print(fruits)
fruits.clear()
print(fruits) 






