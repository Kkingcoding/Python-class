def say_myself(name, age, is_male=True):
    print("My name is %s" % name)
    print("I am %d years old" % age)
    if is_male:
        print("I am a man")
    else:
        print("I am a woman")

# Get user information using input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_gender = input("Enter your gender ('M' or 'm' for male, any other key for female): ")

# Check gender
is_male = user_gender.lower() == 'm'

# Call the function
say_myself(name=user_name, age=user_age, is_male=is_male)