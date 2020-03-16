def my_function():
  print("Hello from a function")
my_function()

#passing arguements
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

#Number of Arguements
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

#Variable length arguements
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

#Keyword arguements

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Variable keyword arguements
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

#Default parameters

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

#list as arguement
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

#return Statement

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

#Lambda function
# x = lambda a : a + 10
# print(x(5))

#More arguements
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))