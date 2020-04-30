names = ['harry', 'larry', 'sherry', 'mary', 'keri']
print(names)

# access each item by index
# for i in range(len(names)):
#     print(names[i])

# iterator (access each item as it is)
# for name in names:
#     print(name)

# add item to end of the list
names.append('barry')
print(names)

#remove an item by index
names.pop(1)
print(names)

#remove an item by specific item
names.remove('sherry')
print(names)

#add an item at a specific index
names.insert(1, 'canary')
print(names)

