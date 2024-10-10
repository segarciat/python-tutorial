def greet(username):
    """
    Displays a personalized greeting.
    
    :param str username: A name as a string.
    """
    print(f"Welcome back, {username}!")

user_input = input("Please enter your name: ")
greet(user_input)