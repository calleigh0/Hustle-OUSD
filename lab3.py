# Lab 3 

# Task 1: Working with Strings
food = "quesa birrias"
print(food)
print(food[0:3]) #first 3
print(food[-3:]) #last 3 
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

# Task 2: Working with Lists
number_list = [1, 7675647456, 32, -5, 0, 234]
number_list.append(67)
print(number_list)
number_list.insert(3, 1000)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(7675647456)
print(number_list)
print(number_list[0:3]) #first 3
print(number_list[-3:]) #last 3 

# Task 3: Working with Dictionaries
books = { "Amy Tan" : "The Joy Luck Club", "Shel Silverstein" : "The Giving Tree",  "George Orwell" : "Animal Farm", "Junot Diaz" : "The Brief wondorous Life of Oscar Wao"}
print(books.keys())
print(books.values())
print(books.get("Junot Diaz"))
books.pop("George Orwell")
print(books)
del books["Amy Tan"]
print(books)
