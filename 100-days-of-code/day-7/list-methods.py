list = ['larry', 'curly', 'moe']

# list.append(elem) -- adds a single element to the end of the list. 
# Common error: does not return the new list, just modifies the original.
list.append('shemp') ## append elem at end

# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.insert(0, 'xxx') ## insert elem at index 0

# list.extend(list2) adds the elements in list2 to the end of the list. 
# Using + or += on a list is similar to using extend().
list.extend(['yyy', 'zzz']) ## add list of elems at end

print(list) ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']

# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
print(list.index('curly')) ## search and remove that element

# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.remove('curly') ## search and remove that element

# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
list.pop(1) ## removes and returns 'larry'
print(list) # ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']


print(list.append(4))
list.append(4)
print(list) ## [1, 2, 3, 4]




## LIST BUILD UP
list = []
list.append('a') ## Use append() to add elements
list.append('b')
print(list)


list = ['a', 'b', 'c', 'd']
print(list[1:-1]) ## ['b', 'c']
list[0:2] = 'z' ## replace ['a', 'b'] with ['z']
print(list) ## ['z', 'c', 'd']

'''
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
list.reverse() -- reverses the list in place (does not return it)

'''

