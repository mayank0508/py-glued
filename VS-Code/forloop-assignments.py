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

n = int(input())

for i in range(1, n+1, 1):
    for s in range(i-1): # this is the code for printing space
        print(" ", end='')
    for j in range(i,n+1, 1):
        print(j, end='')
    print()