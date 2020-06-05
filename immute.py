# Managing immutables in strings

# Note that strings are not mutable and we cant use indexing to change individual elements of a string.
# We can however use concatnation to address immutables in the strings data type

# Define a string variable

name = "Daniel"
# In order to change a character "D" to "V" in string to read "Vaniel,"

#name[0]='V'

"""You might be tempted to change the character using indexing of the string, but this presents an error
because strings are immutable;
ERROR-------
Traceback (most recent call last):
  File "/home/aoaristacus/DevHost/Python/hello/immute.py", line 11, in <module>
    name[0]='V'
TypeError: 'str' object does not support item assignment----
"""
print(name)
# To resolve this, we use CONCATENATION

# Define the line a new variable

newname = name[1:]

print(newname)

print("V"+newname)





