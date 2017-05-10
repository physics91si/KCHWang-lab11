import string

# Returns a list of the first 10 letters of the alphabet.
my_list1 = list(string.ascii_lowercase[0:10])
print("my_list1:")
print(my_list1)

# Returns a list of the first 10 letters of the alphabet except for the sixth letter.
char_not_to_include = my_list1[5]
my_list2 = [char for char in my_list1 if char != char_not_to_include]
print("my_list2:")
print(my_list2)

# Returns a list of the first 10 letters of the alphabet, except the sixth one, each repeated 1, 2, and 3 times.
def once(s):
    return s
def twice(s):
    return s + s
def triple(s):
    return s + s + s

my_list3 = [f(char) for char in my_list2 \
            for f in (once, twice, triple)]
print("my_list3:")
print(my_list3)

# Returns the list like the above, but in a grid.
my_list4 = [[once(char), twice(char), triple(char)] for char in my_list2]
print("my_list4:")
print(my_list4)