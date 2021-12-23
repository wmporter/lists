import os



my_secret = os.environ['TOKEN']
print(my_secret)
# li1 has two lists in it
# The lists are references
li1 = [[1,2],[3,4]]

# When li2 is created, those list references are 
# now in both
li2 = li1[:]

# The lists li1 and li2 have different ids
# which means they are different lists
print('Does id(li1) equal id(li2)?', id(li1) == id(li2))
print('id(li1):', id(li1))
print('id(li2):', id(li2))
print()

# However the lists inside li1 and li2 refer to the same lists
print('Does id(li1[0]) equal id(li2[0])?', id(li1[0]) == id(li2[0]))
print('id(li1[0]):', id(li1[0]))
print('id(li2[0]):', id(li2[0]))
print()

# This means we can alter the list using either reference
# and we will be able to see that change in either li1 or li2
print('Modify the first item list by using li2[0].append(5)')
li2[0].append(5)
print('li1:', li1)
print('li2:', li2)
print()

print('Modify the first item list by using li1[0][1] = 10')
li1[0][1] = 10
print('li1:', li1)
print('li2:', li2)
print()

# But we can also modify the lists li1 and li2 showing that they are separate
# Here we change li1 by adding an item to it. That item is not in li2
print('Modify li1 using li1.append(100)')
li1.append(100)
print('li1:', li1)
print('li2:', li2)
print()

# We can also add an item to li2 which will not show up in li1
print('Modify li2 using li2.append(47)')
li2.append(47)
print('li1:', li1)
print('li2:', li2)
print()

# We can even make a change so that li1[0] and li2[0] are no longer the same reference
print('Modify li1[0] to refer to a new list [7, 8]')
li1[0] = [7, 8]
print('li1:', li1)
print('li2:', li2)
print()

# Now li1[0] and li2[0] no longer refer to the same list, so changes in one won't show in the other
print('Modify li2[0] using li2[0].append(6)')
li2[0].append(6)
print('li1:', li1)
print('li2:', li2)
print()
