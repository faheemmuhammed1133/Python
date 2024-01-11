# demonstrate different methods of list

# creation
l=[1,2,8,9,0,-4,"c","@"]

# l.append adding new item in the list
l.append("p")

# l.extend addimg multiple items in list
l.extend(["a",6])

# l.pop removes "i"th item from the list,default last
l.pop(5)

# l.insert(i,item) insert item at positio i : basically inserts a new item at index i rather than changin the the index i value
l.insert(4,-1)

# l.remove (item)find the item and removes from the list
l.remove("p")
l.remove("a")
l.remove("c")
l.remove("@")
print(l)

# l.sort sort the list in place reverse=True will sort in ascendint order
l.sort(reverse=True)
print(l)