**Day 1: Introduction and Python Installation**

1. Python Installation
   - Install Python from the official website: https://www.python.org/downloads/
   - Install a text editor or an Integrated Development Environment (IDE), like PyCharm or Visual Studio Code.
   - Run your first Python program:
     ```python
     print("Hello, World!")
     ```

Assignment: Write a program that prints your name and age.

**Day 2: Variables and Basic Data Types**

1. Variables
   - A variable is a name that refers to a value.
     ```python
     message = "Hello, Python!"
     print(message)
     ```
2. Data Types
   - Strings, integers, floats, and booleans.
     ```python
     my_string = "Hello, Python!"
     my_int = 10
     my_float = 20.0
     my_bool = True
     ```

Assignments:
1. Create variables of each type (integer, float, string, boolean) and print their type using the `type()` function.
2. Create a string, convert it to an integer and print it.

**Day 3: Strings and Number Operations**

1. Strings
   - Concatenation, indexing, and slicing.
     ```python
     greeting = "Hello"
     name = "Python"
     message = greeting + ", " + name + "!"
     print(message)
     ```
2. Number Operations
   - Addition, subtraction, multiplication, division, exponentiation.
     ```python
     x = 10
     y = 20
     print(x + y)
     print(x - y)
     print(x * y)
     print(x / y)
     print(x ** y)
     ```
Assignments:
1. Concatenate two strings and print the result.
2. Perform different arithmetic operations (addition, subtraction, multiplication, division) on two numbers.

**Day 4: Lists and Tuples**

1. Lists
   - Creating, accessing, modifying, and basic operations on lists.
     ```python
     my_list = [1, 2, 3, 4, 5]
     print(my_list[0])
     my_list[1] = 20
     print(len(my_list))
     print(my_list + [6, 7, 8])
     ```
2. Tuples
   - Creating and accessing tuples.
     ```python
     my_tuple = (1, 2, 3, 4, 5)
     print(my_tuple[0])
     ```

Assignments:
1. Create a list of 5 items, modify the 3rd item and print the list.
2. Create a tuple with your first name and last name, try to modify the first name (to see the error), and print the tuple.

**Day 5: Dictionaries**

1. Dictionaries
   - Creating, accessing, and modifying dictionaries.
     ```python
     my_dict = {"name": "Python", "type": "Programming Language"}
     print(my_dict["name"])
     my_dict["version"] = 3.8
     ```
Assignments:
1. Create a dictionary representing a book, with keys for title, author, and year. Print the dictionary.
2. Add a new key-value pair to the dictionary representing the number of pages in the book.

**Day 6: Conditional Statements**

1. Conditional Statements
   - Using if, elif, and else to control program flow.
     ```python
     x = 10
     if x > 0:
         print("Positive")
     elif x < 0:
         print("Negative")
     else:
         print("Zero")
     ```
Assignments:
1. Write a program that checks if a number is positive, negative or zero.
2. Write a program that takes in a grade (0-100). If it's 90 or above, it's an A. 80-89 is a B. 70-79 is a C. 60-69 is a D. Anything below 60 is an F.


**Day 7: Looping**

1. Looping
   - For loops and while loops.
     ```python
     for i in range(5):
         print(i)
         
     x = 0
     while x < 5:
         print(x)
         x += 1
     ```
Assignments:
1. Use a for loop to print the numbers 1 to 10.
2. Use a while loop to print the numbers from 10 to 1 in descending order


**Week 1 Recap**
Assignments:
1. Create a [bubblesort algorithm](https://www.google.com/search?q=bubble+sort&rlz=1C5CHFA_enUS1003US1003&oq=bubble+sort&aqs=chrome..69i57j0i67i650j0i67i433i650j0i512j0i67i650j0i512l5.1906j0j4&sourceid=chrome&ie=UTF-8)
2. Create a game of tictactoe
  