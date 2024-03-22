"""
1. Briefly explain: what is modular programming?

Modular programming is method of programming that arranges code in to individual modules that have specific roles and
responsibilities within a program. Modular programming is useful for code maintainability, as it allows the updating and
modification of code without having to restructure last amounts of a code base; if implemented properly.


2.How can you import only a specific function or class from a module in Python? What is the syntax for this?

You can use the following syntax for an import statement at the top of a module:
from module.py import specific_function_or_class

3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?
Justify your answer.

I initially think that it would be more like a pass-by-reference, but I also feel that pass-by-value is important here.
Data is stored in the memory and requires a reference/pointer to be retrieved, but that reference also stores a value
that can be utilised in methods and functions of the program. These references can be stored as mutable and immutable
objects and for this reason I think it is a bit of both. An int; once declared must always be an int, but its value can
change as long as its new value is an int. A list however, can contain multiple data types and can be altered within a
function, but if no value is returned to it reference, some or all of the changes will be lost.
So I think it is a bit of both pass-by-reference for the space in memory and pass-by-value for the data in that space.

4. Given the following Python code, what will be the output and why?

    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)

The outcome will be a list that contains ["original", "new"]. The reason for this is that the list object called items
has been passed into the modify_list function as an argument. I note that the parameter in the modify_list function is
not the same as the items argument in modify_items. The function appends "new" to the list_ parameter; of which the
argument items is passed into, so "new" is appended to items.
Next; the function makes a new list object called list_ and assigns ["completely", "new"] to it.
The function then ends and has not returned the new list object list_ and it is discarded.
This is an example of pass-by-reference and then pass-by-value, as the values in items could be modified due to a
reference, but the list_ object was not stored despite being modified.


5. In Python even though variables created within a function are local, there are still situations where you can modify
data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by
reference.

TODO:


6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized
applications?

TODO:

"""