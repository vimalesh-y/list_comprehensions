#####
# Create a list of squares
squares = []
for i in range(1,101):
    squares.append(i**2)

print(squares)

# Printing list of squares using list comprehension
squares2 = [i**2 for i in range(1,101)]
print(squares2)


#####
# Create a list of remainders of 100 squares when dividing by 5 and 11
remainder5 = [x**2 % 5 for x in range(1,101)]
print(remainder5)

remainder11 = [x**2 % 11 for x in range(1,101)]
print(remainder11)

#####
animals = ["dog", "cat", "fox", "cheetah"]
# Without list comprehension
danimals = []
for animal in animals:
    if animal.startswith("d"):
        danimals.append(animal)
print(danimals)

# With list comprehension
danimals = [animal for animal in animals if animal.startswith("d")]
print(danimals)

# Using list copmrehension and tuples with animal and colour
animalcolour = [("dog", "black"), ("cat", "ginger"), ("fox", "brown"), ("cheetah", "orange")]
colour = [colour for (animal, colour) in animalcolour if colour.startswith("b")]
print(colour)

##### Scalar multiplication
v = [2, -3, 1]
w = [4*x for x in v]
print(w)

##### Cartesian product
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cp = [(a, b) for a in A for b in B]
print(cp)
