"""Week 1: ask three questions and display a friendly introduction."""

print("Let's get to know you!")

# input() asks a question and returns the user's answer as text.
name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
hobby = input("What is your favorite hobby? ").strip()
favorite_food = input("What is your favorite food? ").strip()

# An f-string inserts the values of variables inside the braces.
print(f"\n🎉 Welcome, {name}! 🎉")
print(f"You are {age} years old and love {hobby}.")
print(f"Your favorite food is {favorite_food}.")
print("It's great to meet you. Enjoy your Python learning journey!")
