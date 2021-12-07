# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     while(j<=n-i+1):
#         print('*', end='')
#         j = j + 1
#     print()
#     i = i+1

# ****
# ***
# **
# *

################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     j = 1
#     while(j<=n-i+1):
#         print(n-i+1, end='')
#         j = j + 1
#     print()
#     i = i+1

# 4444
# 333
# 22
# 1

##############################################################

# n = int(input())
# i = 1
# while(i<=n):
#     space = 1
#     while(space<= n-i):
#         print(' ', end ="")
#         space = space + 1
#     star = 1
#     while(star <= i):
#         print('*', end='')
#         star = star + 1
#     print()
#     i = i + 1

    #     *
    #    **
    #   ***
    #  ****
    # *****

################################################################3

# n = int(input())
# i = 1
# while(i<=n):
#     space = 1
#     while(space<= n-i):
#         print(' ', end ="")
#         space = space + 1
#     star = 1
#     while(star <= i):
#         print(star,end ='')
#         star = star + 1
#     print()
#     i = i + 1

#     1
#    12
#   123
#  1234

########################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     space = 1
#     while(space<=n-i):
#         print(' ', end="")
#         space += 1
#     j = 1
#     p = 1
#     #increasing sequence
#     while(j <= i):
#         print(p, end="")
#         p += 1
#         j += 1
#     #increasing sequence
#     p = i-1
#     while(p>=1):
#         print(p, end='')
#         p -= 1
#     print()
#     i += 1

#   1
#  121
# 12321 

########################################################################


# n = int(input())
# i = 1
# while(i<=n):
#     space = 1
#     while(space<=n-i):
#         print(' ', end="")
#         space += 1
#     j = 1
#     p = 1
#     #increasing sequence
#     while(j <= i):
#         print(i+p-1, end="")
#         p += 1
#         j += 1
#     #increasing sequence
#     p = i-1
#     while(p>=1):
#         print(i+p-1, end='')
#         p -= 1
#     print()
#     i += 1

#    1
#   232
#  34543
# 4567654

########################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     space = 1
#     while(space<=n-i):
#         print(' ', end="")
#         space += 1
#     #decreasing sequence
#     p = i-1
#     while(p>=1):
#         print(p, end='')
#         p -= 1
#     #increasing sequence
#     j = 1
#     p = 1
#     while(j <= i):
#         print(p, end="")
#         p += 1
#         j += 1
#     print()
#     i += 1

################################################################
# h = int(input("please enter diamond's height:"))

# for i in range(1, h, 2):
#     print(" "*(h//2-i//2), "*"*i)
# for i in range(h, 0, -2):
#     print(" "*(h//2-i//2), "*"*i)

#    *
#   ***
#  *****
#   ***
#    *

################################################################

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end='')
#         j += 1
#     space = 1
#     while space <= 2*n-2*i:
#         print(" ", end='')
#         space += 1
#     p = i
#     while p >= 1:
#         print(p, end='')
#         p -= 1    
#     print()
#     i += 1

################################################################

# n = int(input())
# i = 1
# while i <= n:
#     space = 1
#     while space <= n-i:
#         print(" ", end='')
#         space += 1
#     j = 1
#     while j <= i:
#         print(j, end='')
#         j += 1
#     print()
#     i += 1

################################################################

# n = int(input())
# i = 1
# while(i<=n):
#     space = 1
#     while(space<=n-i):
#         print(' ', end="")
#         space += 1
#     #decreasing sequence
#     p = i
#     while(p>1):
#         print(p, end='')
#         p -= 1
#     j = 1
#     #increasing sequence
#     while(j <= i):
#         print(j, end="")
#         j += 1
#     print()
#     i += 1

#    1
#   212
#  32123
# 4321234

################################################################
# num = int(input())
# for i in range(1,num+1):
#     if i <= round(num/2):
#         for j in range(1,i):
#             print(" ",end="")
#         for j in range(0,i):
#             print("*",end="")
#     else:
#         for j in range(1,num-i+1):
#             print(" ",end="")
#         for j in range(0,num-i+1):
#             print("*",end="")
#     print()

# *
#  **
#   ***
#  **
# *

################################################################

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         if(j == i):
#             print("*", end="")
#         else:
#             print(0, end="")
#         j = j + 1
#     p = i
#     while p <= 1:
#         if(p == i):
#             print("*", end="")
#         else:
#             print(0, end="")
#         p = p+1
#     print()
#     i += 1

################################################################

