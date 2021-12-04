# #print kth alphabet
# k = int(input())
# x = ord('A')
# getChar = x + k - 1
# printChar = chr(getChar)
# print(printChar)

# this above method is used to generate Alphabet from numbers

############################################################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     while(j<=n):
#         CharP = chr(ord('A') + j - 1)
#         print(CharP, end='')
#         j = j + 1
#     print()
#     i = i + 1

    # ABCD
    # ABCD
    # ABCD
    # ABCD   ---> this is the o/p of this code

################################################################################################################    

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     start_char = chr(ord('A') + i - 1)
#     while(j<=n):
#         CharP = chr(ord(start_char) + j - 1)
#         print(CharP, end='')
#         j = j + 1
#     print()
#     i = i + 1
    
    # ABCD
    # BCDE
    # CDEF
    # DEFG

##############################################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     start_char = chr(ord('A') + i - 1)
#     while(j<=i):
#         CharP = chr(ord(start_char) + j - 1)
#         print(CharP, end='')
#         j = j + 1
#     print()
#     i = i + 1
    
    # A
    # BC
    # CDE
    # DEFG

##############################################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     start_char = chr(ord('A') + i - 1)
#     while(j<=i):
#         CharP = chr(ord(start_char))
#         print(CharP, end='')
#         j = j + 1
#     print()
#     i = i + 1

# A
# BB
# CCC

#############################################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     while(j<=n):
#         print(1, end='')
#         j = j + 1
#     print()
#     i = i + 1

#####################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     count = 0
#     while(j<=i):
#         print(1, end='')
#         j = j + 1
#     print()
#     i = i + 1

######################################################################

# n = int(input())
# i = 1
# while(i <= n):
#     j = 1
#     while(j<=n-i+1):
#         print(j, end='')
#         j = j + 1
#     print()
#     i = i + 1

# 1234
# 123
# 12
# 1

######################################################################

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(1,  end='1')
#         j = j + 1
#     print()
#     i = i + 1

# rows = int(input())
# for i in range(1, rows + 1):
#     for j in range(1, i - 1):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()

# def print_pascal_triangle(size):
#     for i in range(0, size):
#         for j in range(0, i + 1):
#             print(decide_number(i, j), end=" ")
#         print()


# def decide_number(n, k):
#     num = 1
#     if k > n - k:
#         k = n - k
#     for i in range(0, k):
#         num = num * (n - i)
#         num = num // (i + 1)
#     return num

# # set rows
# rows = int(input())
# print_pascal_triangle(rows)

###############################

n = int(input())
i = 1
while(i<=n):
    j = 1
    start_char = chr(ord('A') + i - 1)
    while(j<=i):
        CharP = chr(ord(start_char) + j - 1)
        print(CharP, end='')
        j = j + 1
    print()
    i = i + 1