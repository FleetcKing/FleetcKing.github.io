# If you look at the bottom of this script, 
# you'll see a python-specific way to force the main() function to run when the script runs.
# Read through the main() function and go to the specific functions as you are called to.
# Make the changes in the specific functions to pass the tests.
# When you get "All Tests Passed", the crash course is complete.

def main():
    # this is a comment. A comment will be ignored by python
    '''
        You can also use this triple apostrophe to add comments. This is known as a docstring.
    '''

    ### PART 0 ###

    # VSCode and other IDEs will allow you to see the docstring for a function by mousing over.
    # Mouse over the line below to see the description from the module_0_comment() function
    # TODO: Look inside the module_0_comment() function below to see how it works.
    # NOTE: You can use ctrl+click on the function name to move into the actual function.
    module_0_comment()

    # You can also print out the functions docstring using the __doc__ property
    print(module_0_comment.__doc__)
    
    print("-----------------------------------------")


    ### PART 1 ###

    # Functions take arguments as parameters.
    # To clarify, parameters are the names listed in the functions definition.
    # The arguments are the specific values passed to the function. 
    my_name = "" # put your name inside of the quotes
    my_favorite_color = "" # put your favorite color inside of the quotes

    # TODO: Look inside the module_1_parameters() function below to see how it works.

    # in this case, the arguments that are passed are my_name and my_favorite_color
    # the parameters are name and color
    module_1_parameters(my_name, my_favorite_color)

    print("-----------------------------------------")


    ### PART 2 ###

    # As we saw in part 2, functions are able to take values via arguments
    # Functions can also return values at the end.

    # TODO: Read through the module_2_return function. Change the values passed so the returned result is 64
    returned_result = module_2_return(1, 0)
    print(f"The returned result should be 64: {returned_result}")

    print("-----------------------------------------")



    ### PART 3 ###

    # Operators are used to perform operations on variables.
    # Learn about all of the operators that Python can do here:
    # https://www.w3schools.com/python/python_operators.asp

    # TODO: Read through module_3_operators(), and update the code to successfully return the 13.0
    print(f"The answer to this should be 13.0: {module_3_operators(5,12)}")

    print("-----------------------------------------")


    ### PART 4 ###

    # Let's talk about different data types.

    # TODO: Look through the module_4_datatypes() function
    module_4_datatypes()

    print("-----------------------------------------")



    ### PART 5 ###

    # Let's talk about logical and comparison operators

    # TODO: Look through the module_5_logic() function
    print(f"If you completed everything correctly in module 5, this should be True: {module_5_logic()}")


    print("-----------------------------------------")

    ### PART 6 ###

    # Let's talk about conditional statements

    # TODO: Look through the module_6_conditional() function
    print(f"If you completed everything correctly in module 6, this should be True: {module_6_conditional()}")


    print("-----------------------------------------")

    ### PART 7 ###

    # Let's talk about iteration with for loops

    # TODO: Look through the module_7_loops() function
    module_7_loops()

    print("-----------------------------------------")


# ------------ END OF MAIN FUNCTION START OF MODULE FUNCTIONS ---------------- #


def module_0_comment():
    '''
        This is an example of a docstring that explains the purpose of a function.
        The first part of the docstring should describe what the function does.
        For example, this function gives an example of docstrings and what they do.
        Docstrings are not required, but can often be helpful, especially in large projects
        
        Parameters:
            None
        Returns:
            None
    '''
    # there are no tasks to complete in this function
    return None




def module_1_parameters(name, color):
    '''
        Prints out a greeting with the person's name and favorite color.
        
        Parameters:
            name (str): a string of a name
            color (str): a string of a color
        Returns:
            None
    '''

    # TODO: Read through this. There is some complicated code, see if you might be able to figure out what's going on.
    color_objects = {
        "red": "an apple",
        "green": "grass",
        "blue": "the ocean",
        "purple": "a grape",
        "orange": "an orange",
        "yellow": "the sun",
        "pink": "an azalea",
        "black": "the void",
        "grey": "a wolf",
        "gray": "a wolf",
        "white": "a cloud"
    }

    if color.lower() in color_objects:
        color_object = color_objects[color.lower()]
    else:
        color_object = "something cool"

    # the 'f' in front of the string indicates something called string formatting
    # string formatting allows you to plug variables into a string.
    print(f"Hello, {name}! Your favorite color is {color.lower()} like {color_object}.")




def module_2_return(a, b):
    '''
        Takes to values, a and b, return a to the power of b
        
        Parameters:
            a (int): the base
            b (int): the exponent
        Returns:
            (int) a to the power of b
    '''
    return a**b




def module_3_operators(a, b):
    '''
        Solves the pythagoreon theorem
        Takes a and b which are the sides adjacent to the 90 degree angle in a right triangle,
        solving for c
        
        Parameters:
            a (float): side 1
            b (float): side 2
        Returns:
            (float): length of hypotenuse
    '''
    # pythagrean theorem: a^2 + b^2 = c^2
    # sum: x + y
    # dif: x - y
    # prod: x * y
    # quot: x / y
    # remainder (modulo): x % y
    # power: x ** y
    # square: x**2
    # square root: x**0.5
    # use parenthesis to dictate order of operations
    # example: (x + y) * z

    # TODO: Change None to return the value of c, given a and b
    return None 

        

def module_4_datatypes():
    '''
        Gives a tutorial of Python data types
        
        Parameters:
            None
        Returns:
            None
    '''
    
    # 1. Boolean
    # A boolean (or binary) value can only be represented in two ways
    # Some languages use a 0 or 1, but most use True or False
    my_bool = True
    your_bool = False


    # 2. Integer
    # an integer is a whole number. It is represented in python by writing the number without quotes
    x = 10

    # 3. Float
    # a float (or floating point number) is a number that may have decimals.
    # when two integers are divided, the result is automatically cast as a float
    y = 0.5

    # 4. Character
    # a character is a single character.
    # they include letters, numbers, punctuation, blank spaces, line breaks, or any other symbol.
    # They can be surrounded by single apostophes or double quotes
    c = "!"

    # 5. String
    # a string is a series of characters that may form a word or sentence.
    # this follows the same rules as a character.
    s = "My String."


    # 6. List
    # a list (sometimes called arrays in other languages) are a series of other data types groupped together
    my_string_list = ["This", "is", "a", "list", "."]
    my_integer_list = [0,8,12,-4,7]
    my_mixed_list = ["Hi", 4.25, "%", 10]

    # 7. Dictionary
    # a dictionary is similar to a list, but it holds key, value pairs.
    # Think of it like a dictionary, where you can look up a word (key) and find a definition (value)
    my_dict = {"sample_key": "sample_value", "name": "Dan", "age": 25, "job": "teacher"}

    # For a more in-depth look at Python Data types, see:
    # https://www.w3schools.com/python/python_datatypes.asp




def module_5_logic():
    '''
        This function teaches how to use comparison and logical operators in Python
        
        Parameters:
            None
        Returns:
            (boolean) True if you answered everything correctly, False if not
    '''

    # Comparison operators compare two values. Comparison always parses as a boolean (True or False)

    # == compares two things for equality
    # example: x == y
    5*2 == 10 # this would be True
    5*3 == 14 # this would be False

    # >, >=, <, <= Greater than, greater than or equal to, less than, less than or equal to
    # example: x <= y

    5*4 <= 20 # this would be True
    5*4 < 20 # this would be False
    5*5 >= 26 # this would be False
    5*5 > 24 # this would be True

    # != compares two things for inequality
    # parses as True if they are NOT equal, false if they are
    # example: x != y

    5*6 != 30 # this would be False
    5*6 != 29 # this would be True


    # Logical Operators combine comparison operators

    # and: returns True if BOTH statements are True
    # example: x==y and z != w

    5*6 == 30 and 5*7 == 35 # this would be True, because both are True
    5*8 == 40 and 5*9 == 46 # this would be False, because one is True and one is False
    5*10 == 49 and 5*11 == 54 # this would be False, because both are False

    # or: returns True if EITHER of the statements are True
    # example: x == y or z != w

    5*6 == 30 or 5*7 == 35 # this would be True, because both are True
    5*8 == 40 or 5*9 == 46 # this would be True, because one is True and one is False
    5*10 == 49 or 5*11 == 54 # this would be False, because both are False

    # not: inverts the result of any logical or comparison operators
    # example: not(x == y)

    not 5*2 == 10 # False, because the original condition is True
    not 5*4 < 20 # True, because the original condition is False
    not 5*6 != 29 # False, because the original condition is True (double negative...)
    not 5*6 == 30 and 5*7 == 35 # False, because the original condition is True
    not 5*8 == 40 and 5*9 == 46 # True, because the original condition is False


    # TODO: your answers should match the questions
    # example:
    question_0 = 10*2 == 20
    answer_0 = True

    # Change all of the None to the correct answer

    question_1 = 5*6 == 29
    answer_1 = None

    question_2 = 10 != 11
    answer_2 = None

    question_3 = 2*6 >= 11
    answer_3 = None

    question_4 = 2+2 == 4 and 3+3 == 5
    answer_4 = None

    question_5 = 2+3 == 4 or 3+3 == 6
    answer_5 = None

    question_6 = 2 > 1 and not 10 != 10
    answer_6 = None

    return question_1 == answer_1 and question_2 == answer_2 and question_3 == answer_3 and question_4 == answer_4 and question_5 == answer_5 and question_6 == answer_6




def module_6_conditional():
    '''
        This function teaches how to use conditional statements in Python
        
        Parameters:
            None
        Returns:
            None
    '''

    # conditional statements are used in conjunction with comparison/logical operators
    # this allows you to run code only if a boolean condition is met.
    print("MODULE 6 STUFF")
    if True:
        print("This will print")

    if False:
        print("This will not print")

    
    # else can be used to run code only if the first condition is not met
        
    if False:
        print("This also won't print")
    else:
        print("This also will print")

    # elif (short for else+if) can be used to test a second condition. This will only run if the first condition wasn't met
    
    if True:
        print("This also will print, as well.")
    elif True:
        print("This will not print because the first condition was met.")

    if False:
        print("This will not print, because the condition wasn't met.")
    elif True:
        print("This will print, because the first condition was not met, and this one was.")

    # else can be used along with elif

    if False:
        print("This will not print, because the condition wasn't met.")
    elif False:
        print("This also will not print, because the condition wasn't met.")
    else:
        print("This will print because the other two conditions were not met.")

    # TODO: Figure out what the result_number is and write my_number to match it.
        
    result_number = 10

    if result_number > 10:
        result_number = result_number*2
    elif result_number == 10:
        result_number = result_number - 5
    elif result_number > 4:
        result_number = 6
    else:
        result_number = 3

    # change this to match result_number
    my_number = None


    
    return my_number == result_number
    


def module_7_loops():
    '''
        This function teaches how to use for and while loops in Python
        
        Parameters:
            None
        Returns:
            None
    '''

    # For loops are used to iterate through a list if items.
    
    my_shopping_list = ["apples", "bananas", "cherries", "dog treats", "edamame", "falafel"]

    print("MODULE 7 STUFF")
    for item in my_shopping_list:
        print(f"{item} is on my shopping list!")

    # while loops will run as long as a comparison is True
    
    counter = 1

    while counter < 10:
        print(f"The number is now {counter}.")
        counter = counter + 1

    
        
    # There are also special keywords that can be used within loops
    # pass: doesn't do anything, just lets the code run as it was before. Often used as a filler while figuring out how to handle a situation
    # continue: does not complete the rest of the code in the loop, instead moves to the next iteration
    # break: does not complete the rest of the code in the loop, instead immediately breaks out of the loop

    my_num = 1
    while True: # while True is dangerous, as it will run forever, but we can use break to get out of it.
        my_num = my_num * 2 # doubles my_num
        print(f"This doubling number is now {my_num}.")
        # we can use the condtional to break out of the loop
        if my_num > 100:
            break


    # TODO: Run the code and see what prints out.


    

# This tells the program to run the main function first
if __name__ == "__main__":
    main()
