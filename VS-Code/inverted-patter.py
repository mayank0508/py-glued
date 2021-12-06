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

n = int(input())
i = 1
while(i<=n):
    space = 1
    while(space<= n-i):
        print(' ', end ="")
        space = space + 1
    star = 1
    while(star <= i):
        print('*', end='')
        star = star + 1
    print()
    i = i + 1

    #     *
    #    **
    #   ***
    #  ****
    # *****