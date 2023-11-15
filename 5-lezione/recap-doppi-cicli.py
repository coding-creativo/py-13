# for i in range(1,11): # i = 2
#     for j in range(1,11): #j = 1
#         print('*',end="\t")
#     print()


# * i = 0 j = 1
# ** i = 1 j = 2
# *** i = 2 j = 3
# **** i = 3 j = 4
# ***** i = 4 j = 5

# n = 5 - j = i + 1
n = 5
for i in range(n): # i = 4
    for j in range(i + 1): # j = 5
        print('*', end="")
    print()
