"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Name, age, city, country of a person
# 2. Process: Create a dictionary with the person's information
# 3. Out: Display the person's information  
# 4. My object, my five fields, and why those: I described a person with the fields name, age, city, and country because these are common attributes used to describe an individual in various contexts, such as forms, profiles, or databases.


# Your code below
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

print("My name is", name)
print("My age is", age)
print("My city is", city)
print("My country is", country)


person = {
    "name": name,
    "age": age,
    "city": city,
    "country": country,
}

print("the person name is:", person["name"])
print("the person age is:", person["age"])
print("the person city is:", person["city"])
print("the person country is:", person["country"])  

person_age = person.pop("age")
print("the person age is:", person_age)
print("the person name is:", person["name"])