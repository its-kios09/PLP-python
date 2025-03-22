
# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
def collect_person_info():
    person = {}

    # Collect user input
    person["name"] = input("Enter your name: ")
    person["age"] = int(input("Enter your age: "))  # Convert input to an integer
    person["favorite_color"] = input("Enter your favorite color: ")

    # Print the dictionary
    print("\nPerson Information:")
    print(person)

collect_person_info()
