# n = int(input())
# reg = True
# k = 2

# for i in range(n, 0, -1):
#     for j in range(i, 2*i, 1):
#         if k%2==0:
#             print(1, end='')
#         else:
#             print(0, end='')
#     print()
#     k += 1

# 1111
# 000
# 11
# 0

################################################################

# n = int(input())


# for i in range(1, n+1):
#     count = 1
#     for s in range(1,i): # this is the code for printing space
#         print(" ", end='')
#         count += 1
#     num = i
#     for j in range(count,n+1):
#         print(num, end='')
#         num += 1
#     print()
# for i in range(n-1, 0, -1):
#     count = 1
#     for s in range(1,i): # this is the code for printing space
#         print(" ", end='')
#         count += 1
#     num = i
#     for j in range(count,n+1):
#         print(num, end='')
#         num += 1
#     print()

# 1234
#  234
#   34
#    4
#   34
#  234
# 1234    

################################################################################

n = int(input())
i = 1
while i <= 2*n-1:
    j = 1
    while j <= 2*n-1:
        print(n, end='')
        j += 1
    print()
    i += 1
