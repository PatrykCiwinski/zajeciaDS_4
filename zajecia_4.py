# tools = ['lornetka', 'lupa', 'teleskop', 'sonda']
#
# tools.insert(2,'śrubokręt')
# tools.append('drewno')
# tools+=['gwóźdź']
# tools[2]='kierownica'
# del tools[3]
# tools.pop(3)
# print(tools)
#
# num = [1,2,3,4,5]
# letters=['a','b','c','d']
#
# num.extend(letters)
# print(num)
#
# nums = [1,2,3,4,5]
# even = list(filter(lambda x:(x%2==0),nums))
# print(even)
# print()
# for num in nums:
#     print(num)
# print()
# [print(num) for num in nums]
#
# nums_reversed=nums[::-1]
# print(nums_reversed)
# #or
# nums.reverse()
# print(nums)
#
#
# numbers = [3,15,11,6,1,2,3,0,123,24]
#
# print(sorted(numbers))
# numbers.sort()
# print(numbers)
# # if reverse=True, in other way around

# lt=[(1,4,7),(4,5,1),(77,2,9),(2,3,5)]
# zy =[]
# for t in lt:
#     sum=0
#     for e in t:
#         sum+=e
#     zy.append(sum)
# print(sorted(zy))

#easier
# lt=[(1,4,7),(4,5,1),(77,2,9),(2,3,5)]
# sums=[]
# for el in lt:
#     s= sum(el)
#     sums.append(s)
#
# print()
# print(sorted(sums))

#Głęboka kopia - różne id, zmieniając element listy pochodnej, nie zminiam  elementu listy źródłowej
"""a =[1,2,3,4]
b = a[:]
print(id(a))
print(id(b))"""

#Płytka kopia -  te same id, zmieniając element listy pochodnej, zminiam  elementu listy źródłowej

"""a =[1,2,3,4]
b = a
print(id(a))
print(id(b))"""

#Deep copy list of list - pomimo różnych id ,obie listy są zmieniane gdy zieniamy element jednej listy
vechicles1 = [['fiat', 'ferrari', 'opel', 'skoda'], ['car', 'bolid', 'gokart']]
vechicles2 = vechicles1[:]

vechicles2[1].append('rolki')
vechicles1[1].append('rower')
print(id(vechicles1))
print(id(vechicles2))


import copy

# Płytka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.copy(l1)

l1[1][1] = 'SHALLOW'

print(l1)
print(l2)

print(id(l1))
print(id(l2))


# Płytka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.copy(l1)

l1[1][1] = 'SHALLOW'

print(l1)
print(l2)

print(id(l1))
print(id(l2))

# Głeboka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.deepcopy(l1)

print(l1)
print(l2)

l1.append([10, 11, 12])

print(l1)
print(l2)

print(id(l1))
print(id(l2))


# Głęboka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.deepcopy(l1)

l1[1][1] = 'DEEPCOPY'

print(l1)
print(l2)

print(id(l1))
print(id(l2))



