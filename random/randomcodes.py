# mylist = [34, 64, 25, 12, 22, 11, 90, 5]

# n = len(mylist)
# for i in range(1,n):
#   for j in range(n-i):
#     if mylist[j] > mylist[j+1]:
#       mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# print(mylist)

# l = [34, 64, 25, 12, 22, 11, 90, 5]
# l.reverse()
# print(l)
# d = {'a': 1, 'b': 2, 'd': 3}
# d2 = {'d': 4, 'e': 5}
# concatdict  = {**d, **d2}
# for k,v in d2.items():
#     for k1,v1 in d.items():
#         if k in d:
#             concatdict[k] = v1+v
# print(concatdict)
# print("Welcome to freddy fazbear lets play a game!")
# print("if you meet any of the animatronics you can decide what to do")
# print("""meeting freddy is an instant game over
# meeting bonnie you can either run or hide
# meeting chica you can either run or hide
# meeting foxy is another instant game over""")

# print("at every turn you can either move forward or stay still")
# print("if you stay still there is a 10% chance of either bonnie or chica appearing")
# print("""if you move forward there is a chance than either freddy or foxy might take a movement towards you
# flash light has a 70% chance of scaring away bonnie or chica
# the office is 25 positions away from the starting point
# reach the office to win
# read the rulebook below to understand the game better""")
# print("__________________________________________________________________________________________")
# print(""" RULEBOOK
# 1. You start at position 0 and the office is at position 25
# 2. You can either move forward or stay still at each turn
# 3. If you stay still there is a 10% chance of either bonnie or chica appearing
# 4. If you move forward there is a chance than either freddy or foxy might take a movement towards you
# 5. Freddy and foxy move faster than you so be careful
# 6. If you meet freddy or foxy its an instant game over  """)

# l = [lambda arg = x: arg*10 for x in range(1,6)]
# for thing in l:
#     print(thing())

# mylist = [64, 34, 25, 5, 22, 11, 90, 12]

# n = len(mylist)
# for i in range(n-1):
#   min_index = i
#   for j in range(i+1, n):
#      if mylist[j] < mylist[min_index]:
#        min_index = j
#   min_value = mylist.pop(min_index)
#   print(mylist)
#   mylist.insert(i, min_value)
#   print(mylist)

# print(mylist)




# l = [64, 34, 25, 12, 22, 11, 90, 5]
# def binarysearch(l, target):
#     l.sort()
#     low = 0
#     high = len(l) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if l[mid] == target:
#             return mid
#         elif l[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# print(binarysearch(l,22))

# def bubblesort(l):
#     n = len(l)
#     for i in range(1,n):
#         for j in range(n-i):
#             if l[j] > l[j+1]:
#                 l[j], l[j+1] = l[j+1], l[j]
#     return l
# print(bubblesort(l))

# def selectionsort(l):
#     n = len(l)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1, n):
#             if l[j] < l[min_index]:
#                 min_index = j
#         if min_index != i:
#             l[i], l[min_index] = l[min_index], l[i]
#     return l
# print(selectionsort(l))

# def insertionsort(l):
#     n = len(l)
#     for i in range(1,n):
#         j = i 
#         while l[j-1] > l[j] and j > 0:
#             l[j], l[j-1] = l[j-1], l[j]
#             j -= 1


# def mergesort(l):
#     if len(l) > 1:
#         mid = len(l) // 2
#         L = l[:mid]
#         R = l[mid:]

#         mergesort(L)
#         mergesort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 l[k] = L[i]
#                 i += 1
#             else:
#                 l[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             l[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             l[k] = R[j]
#             j += 1
#             k += 1
#     return l




# l1 = [[1, 4,2], [3,3, 4], [5,4, 6]]
# for i1,i2,i3 in l1:
#     print(i1,i2,i3)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# u = tuple(zip(questions, answers))
# print(u)

# l2 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# for i1,i2 in l2:
#     print(i1,i2)
    # for j1, j2 in i1:
    #     print(j1, j2)
    # for k1, k2 in i2:
    #     print(k1, k2)

#Approximation of pi 
# import random
# inside = 0
# total = 1000
# pi = 0
# count = 0
# while pi <=3.1:
#     x = random.random()
#     y = random.random()
#     if x**2 + y**2 <= 1:
#         inside += 1
        
#     pi = (inside / total) * 4
#     count+=1
#     total += 100
# print(pi)





# userinp = 'workbook 20 50 10 pencil 40 70 90 books 90 100 70'
# userlist = userinp.split()
# print(userlist)

# items = userlist[0::4]
# cost = userlist[1::4]
# sell = userlist[2::4]
# units = userlist[3::4]

# profit = list(map(lambda i:(int(sell[i]) - int(cost[i])) * int(units[i]) , range(len(items))))
# print(profit)



# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# fact(9)


# def fun (x,y=50):
#     return x+y
# fun(20)
# print(fun(20,100))

# y = "This research looks at how two big climate problems — the melting of the cryosphere (ice sheets, glaciers, and permafrost) and the instability of the carbon cycle — are connected and how they affect Earth’s climate. It also links to the UN Sustainable Development Goals, mainly SDG 13 (Climate Action), SDG 14 (Life Below Water), and SDG 15 (Life on Land). The study focuses on how glaciers melt not only from the surface but also from below, where meltwater travels through cracks, moulins, and small water pockets. This process can make glaciers move faster and speed up ice loss. Another part of the research looks at feedback loops like methane release from thawing permafrost and oxygen loss in oceans, which can make global warming worse. By comparing these issues with past events like the Permian extinction and the Snowball Earth period, this study tries to understand how Earth’s systems might react to future climate changes. The goal is to identify possible tipping points, improve climate predictions, and help in making better policies to protect the planet, especially for regions that are most at risk from these rapid environmental changes."
# x = y.split()
# print(len(x))

# import numpy as np

# # Input number of participants
# N = int(input())

# # Input frequencies
# freq_list = [int(input()) for _ in range(N)]

# # Convert to NumPy array
# fre_array = np.array(freq_list)

# # Remove any single-dimensional entries
# fre_array_squeezed = np.squeeze(fre_array)

# # Sort the array
# fre_array_sorted = np.sort(fre_array_squeezed)

# # Expand the array shape (though not needed for quartile calc, per problem statement)
# fre_array_expanded = np.expand_dims(fre_array_sorted, axis=0)

# # Calculate quartiles
# Q1 = np.percentile(fre_array_sorted, 25)
# Q2 = np.percentile(fre_array_sorted, 50)
# Q3 = np.percentile(fre_array_sorted, 75)

# # Output
# print("First Quartile (Q1):", Q1)
# print("Second Quartile (Q2):", Q2)
# print("Third Quartile (Q3):", Q3)
import pandas as pd
# n = int(input())
# data = [input().split() for _ in range(n)]
# df = pd.DataFrame(data, columns=["User_ID", "Enrollment_Date"])
# # print(df)
# import numpy as np
# arr = np.array([1, 2, 3])
# print(np.argwhere(arr % 2 == 0))
# data = [101]
# ser = pd.Series(data)
# print(ser)
# # print(ser.loc[1])
# data = {'name': ["Jeremy","jackslaw","jorbian"], 'age': [41, 52, 46],'profession': ["chef","butcher","baker"]}
# sorted_data = pd.DataFrame(data).sort_values(by=['age'])
# print(sorted_data)
# print(pd.DataFrame(data))
# import numpy as np
# # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # df = pd.DataFrame(arr)

# # df[1][2] = 20
# # print(df)


# userinp = input("enter list")
# print(type(userinp))
# for i in userinp:
#     print(i)


# import random

# def quantum_rng(bits=100):
#     return ''.join(str(random.choice([" ", "O"])) for _ in range(bits))

# for i in range(100):
#     print(f"Random Bit String {i+1}:", quantum_rng())
# # print("Quantum Random Bit String:", quantum_rng())

import matplotlib.pyplot as plt

# Fixed initial level
initial_n = int(input("Enter initial energy level (n): "))
max_n = initial_n - 1

if initial_n <= 1:
    print("Initial level must be greater than 1.")
    exit()

# Energy formula
def energy(n):
    return -13.6 / (n**2)

final_levels = list(range(1, initial_n))
energy_released = []

for f in final_levels:
    delta_E = abs(energy(f) - energy(initial_n))
    energy_released.append(delta_E)

# Plot
plt.plot(final_levels, energy_released, marker='o')
plt.xlabel("Final Energy Level (n)")
plt.ylabel("Energy Released (eV)")
plt.title(f"Energy Released for Electron Falling from n={initial_n}")
plt.grid(True)

plt.show()
