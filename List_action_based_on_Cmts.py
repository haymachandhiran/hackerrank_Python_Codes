# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# # Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# Sample Input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
#
# Sample Output:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
N = int(input())
mylist= []
for i in range(N):
  action, *args = input().split()
  if len(args) > 1:
    arg1, arg2 = [i for i in args]
    arg1 = int(arg1)
    arg2 = int(arg2)
  elif len(args) == 1:
    args[0] = str(args[0])
    arg = int(''.join(args))
  if action == 'insert':
    mylist.insert(arg1, arg2)
    continue
  if action =='print':
    print(mylist)
    continue
  if action == 'remove':
    mylist.remove(arg)
    continue
  if action == 'append':
    mylist.append(arg)
    continue
  if action == 'sort':
    mylist.sort()
    continue
  if action == 'pop':
    mylist.pop(-1)
    continue
  if action == 'reverse':
    mylist.reverse()
    continue
