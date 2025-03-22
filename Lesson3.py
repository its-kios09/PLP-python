# list - data structures - are mutable
list_a = [1, 2, 3, 4, 5]
print(">>>list<<<<<", list_a)

# accessing the elements we use the indexing example as below

print(">>>>indexing<<<<<<",list_a[4])

# assigning a new variable
list_a[4] = 10
print('>>>>>>>appending<<<<<<<<', list_a)

#printing the length
print('>>>>>>length<<<<<<', len(list_a))

#appending a element
list_a.append(50)
print("appending the list>>>>>>", list_a)

#deleting the element
list_a.pop(5)
del list_a[0]
print("deleting the element", list_a)

#looping through a list
for items in list_a:
    print('>>>', items)

# sets are unique set of elements in
student_id = {112, 114, 116, 118, 117}
print('sets of students ids', student_id)

student_id.add(122222)

print('sets of students ids', student_id)

