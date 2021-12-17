# # # Is the number Prime or Not

# # def isPrime(n):
# #     for i in range(2, n):
# #         if (n%i==0):
# #             break
# #     else:
# #         return True
# #     return False

# # # print(isPrime(4))

# # ########################################################################

# # # Print all the prime numbers till the end 

# # def Primetill(n):
# #     for i in range(2, n+1):
# #         is_Prime = isPrime(i)
# #         if is_Prime:
# #             print(i)

# # print(Primetill(20))

# ################################################################################################




# def printTable(start,end,step):
#     s = start
#     e = end
#     st = step
#     for i in range(s,e+1,st):
#         x = (5/9)*(i - 32)
#         z = int(x)
#         print(i, z)

#     pass 

	   
# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s,e,step)


######################################################################


# def checkMember(n):
#     c=0
#     a=1
#     b=1
#     if n==0 or n==1:
#         print("Yes")
#     else:
#         while c<n:
#             c=a+b
#             b=a
#             a=c
#     if c==n:
#         return True

# n=int(input())
# if(checkMember(n)):
#     print("true")
# else:
#     print("false")


