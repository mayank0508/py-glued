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
