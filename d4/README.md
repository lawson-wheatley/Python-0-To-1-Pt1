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

## **Differences between Lists & Tuples**
**Mutability**
- Lists are mutable, which means you can change their content without changing their identity. You can modify a list by adding, removing, or changing elements.

  ```python
  list_example = [1, 2, 3]
  list_example[0] = 100  # This is valid
  ```

- Tuples are immutable, which means once a tuple is created, you cannot change its content.

  ```python
  tuple_example = (1, 2, 3)
  tuple_example[0] = 100  # This will raise an error
  ```

**Use Cases**
- Lists are typically used for collections of items that are similar in nature and are manipulated often during the course of a program. For example, a list of user names or a list of integers.

- Tuples are typically used for collections of items that are different but related. A common use case is for a function to return multiple values. Because tuples are immutable, they can also be used as dictionary keys, which lists cannot.

**Syntax**
- Lists are defined by enclosing a comma-separated sequence of objects in square brackets `[]`.

  ```python
  list_example = [1, 2, 3]
  ```

- Tuples are defined by enclosing a comma-separated sequence of objects in parentheses `()`.

  ```python
  tuple_example = (1, 2, 3)
  ```

**Methods**
- Lists have several built-in methods like append(), insert(), remove(), sort(), and reverse() that can be used to manipulate and modify the list.

- Tuples have fewer handy methods available, due to their immutability, with the most commonly used ones being count() and index().

**Memory and Performance**
- Tuples can be more memory efficient and faster (for some operations) than lists due to their immutability. If you have data that doesn't need to change, using a tuple can be more efficient.



## **Differences between Square Brackets and Parentheses**
**Square Brackets `[]`:**
- **Lists:** Square brackets are used to define lists, which are mutable sequences of elements.
    ```python
    my_list = [1, 2, 3, 4, 5]
    ```
- **Indexing or Slicing:** Square brackets are also used for indexing and slicing operations on lists, strings, tuples, and other sequences.
    ```python
    print(my_list[0])  # Output: 1
    print(my_list[1:3])  # Output: [2, 3]
    ```
- **Dictionary Keys:** You use square brackets to define keys in dictionary definitions, and to access the values associated with those keys.
    ```python
    my_dict = {'name': 'Alice', 'age': 25}
    print(my_dict['name'])  # Output: 'Alice'
    ```
    
**Parentheses `()`:**
- **Tuples:** Parentheses are used to define tuples, which are immutable sequences of elements.
    ```python
    my_tuple = (1, 2, 3, 4, 5)
    ```
- **Function or Method Calls:** Parentheses are used to call a function or method, and to enclose any arguments to the function.
    ```python
    print('Hello, world!')
    ```
- **Order of Operations:** In mathematical operations, parentheses are used to specify the order in which operations are carried out.
    ```python
    result = (1 + 2) * 3  # Output: 9
    ```

**Note:** Lists are defined with square brackets `[]`, but you can also access list items using square brackets. Similarly, tuples are defined using parentheses `()`, but you don't have to use parentheses to access tuple items; you still use square brackets for that.