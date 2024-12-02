# Get to know: Lists
# Key property: Lists are dynamically resized in Python, there's no bound for how many
# elements can be added to a list.

# Syntax for instatiating a list
b = [100,200]
a = [2,4,3] + b # Concat [2, 4, 3, 100, 200]
print(a)
a = [100,2] * 8 # [100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2]
print(a)

# Basic operations
print(len(a))
a.append(42)
print(a)
a.remove(2) # Removes first instance [100, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2...
print(a) 
a.insert(3,28) # Inserts 28 at index 3 (moving to the right the other nums)
print(a)

# Instantiate 2D array
a = [[1,2,3],[4,5,6],[7]]
print(a)
print(7 in a) # Check whether a value is in a
print([7] in a) # Check whether a value is in a

# Understand how copying works
a = [2, 4, 3, 100, 200]
b = [2, 4, 3, 100, 200]
print("\nCopying")
print(b == a)
print(b == list(a))
print(b == list([2, 4, 3, 100, 200]))
# Deep copy vs shallow copy
import copy

print("Deep copy vs Shallow copy")
original = [[1,2],[3,4]]
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)

shallow_copy[1][1] = 200 # Editing an element inside this shallow copy edits those 
                         # elements in the original as well
deep_copy[0][0] = 88
shallow_copy.append([1])

# B = A both reference the same memory location
c = original
c.append([900,700])

# B = list(A) creates a shallow copy
c = list(original)
c[0][0] = 0

print(original) 
print(shallow_copy) # Copies the outer element but doesn't recursively copy the nested ones
print(deep_copy)
print(c)

c = original

