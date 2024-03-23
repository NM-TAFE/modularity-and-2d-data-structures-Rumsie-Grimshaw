"""
1. Briefly explain: what is modular programming?

Answer:
Modular programming is method of programming that arranges code in to individual modules that have specific roles and
responsibilities within a program. Modular programming is useful for code maintainability, as it allows the updating and
modification of code without having to restructure last amounts of a code base; if implemented properly.


2.How can you import only a specific function or class from a module in Python? What is the syntax for this?

Answer:
You can use the following syntax for an import statement at the top of a module:
from module.py import specific_function_or_class


3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?
Justify your answer.

Answer:

I initially think that pythons parameter-passing mechanism is more like a pass-by-reference, but I also feel that
pass-by-value is important here.
Data is stored in the memory and requires a reference/pointer to be both stored and retrieved, but that reference can
also be copied as a value; and used in functions and methods as a parameter.
Pass-by-value creates a copy of data that is stored in a reference/pointer, whereas pass-by-reference refers to the
location in memory of the data itself.
Mutable objects such as lists or dictionaries can be altered in functions that call a reference as an argument, and use
that reference as a parameter or value. Within the scope of the function, the parameter can be altered and still make
changed to the original object as it has been directly referenced. However, the value of the object can be exclusively
manipulated within the functions local scope; and discarded if not returned to the reference/pointer in memory.
In summary - I think it is a little bit of both, referencing the original object outside the scope of the function, and
making a copy of the object within the function.


4. Given the following Python code, what will be the output and why?

    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)

Answer:
The outcome will be a list that contains ["original", "new"]. The reason for this is that the list object called items
has been passed into the modify_list function as an argument.
I note that the parameter in the modify_list function is not the same as the items argument in modify_items.
The function appends "new" to the list_ parameter; of which the argument items is passed into, so "new" is appended
to items.
Next; the function makes a new list object called list_ and assigns ["completely", "new"] to it.
The function then ends and has not returned the new list object list_ and it is discarded.
This is an example of pass-by-reference and then pass-by-value, as the values in items could be modified due to a
reference, but the list_ object was not stored despite being modified.


5. In Python even though variables created within a function are local, there are still situations where you can modify
data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by
reference.

Answer:
If the reference is a mutable object such as a list and the function uses this reference as a parameter;
it can make changes to the parameter that will transfer to the object outside the scope of the function,
as the function is receiving the direct reference of the mutable object and not a copy of it. This is different from
pass-by-value; where the value is a copy of the objects data, not a reference to the object itself.


6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized
applications?

Answer:
Modular programming practices allows a developer to categorise the functionality and responsibility of a module to
contain code specific to its purpose, which helps with readability and the understanding of program logic.

Having multiple modules that are combined within a main module allows individual developers to work on different
modules simultaneously to implement changes as opposed to working from a single module that handles all responsibility.
This allows for changes to be limited to the module only when make revisions, versus the entire code base.
"""