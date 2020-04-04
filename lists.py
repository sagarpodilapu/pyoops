import random


randomlist = random.sample(range(5, 100), 10)
print(randomlist)
print(randomlist[0])
print(randomlist[3])

new_list = ["sagar", randomlist]

print(new_list)
print(new_list[0][2])
print(randomlist[-1])
print(randomlist[-8])
slicing
print(randomlist[3:7])
print(randomlist[:3])
print(randomlist[3:])
print(randomlist[:])
print(randomlist[-7:7])
print(randomlist[7:8])
randomlist[0] = 20
randomlist[2:6] = [30, 40, 50, 60]
randomlist.append(70)
randomlist.extend([80, 90, 100])
randomlist = randomlist + [110, 120, 130]
randomlist = randomlist * 3
del randomlist[2]
del randomlist[3:5]
del randomlist
print(randomlist)
my_list = ["a", "e", "i", "o", "u"]
print(my_list)
my_list.remove("o")
my_list.pop(1)
my_list.clear()
print(my_list)
randomlist = [10, 20, 40, 70, 90, 110, 70]
print(randomlist)
print(randomlist.index(70))  # gives the first index
print(randomlist.count(70))  # counts the number of times
randomlist.sort()
print(randomlist)
randomlist.reverse()
print(randomlist)
