# # # def F(n):
# # #     if(n == 1):
# # #         return 1
# # #     elif(n == 2):
# # #         return 1
# # #     else:
# # #         return F(n-1) + F(n-2)

# # # n = int(input())
# # # print(F(n))

# # # Program to display the Fibonacci sequence up to n-th term

# # nterms = int(input())
# # n1, n2 = 1, 1
# # count = 0

# # # check if the number of terms is valid
# # if nterms <= 0:
# #    print("Please enter a positive integer")
# # # if there is only one term, return n1
# # elif nterms == 1:
# #    print("Fibonacci sequence upto",nterms,":")
# #    print(n1)
# # # generate fibonacci sequence
# # else:
# #    while count < nterms:
# #        print(n1)
# #        nth = n1 + n2
# #        # update values
# #        n1 = n2
# #        n2 = nth
# #        count += 1

# n = int(input("Enter the value of 'n': "))
# a = 0
# b = 1
# sum = 0
# count = 1
# print("Fibonacci Series: ", end = " ")
# while(count <= n):
#   print(sum, end = " ")
#   count += 1
#   a = b
#   b = sum
#   sum = a + b
def Fibonacci(number):
           if(number <= 0):
                      print("Invalid Fibonacci number")
           elif(number == 1):
                      return 1
           elif(number == 2):
                      return 1
           else:
                      return (Fibonacci(number - 1)+ Fibonacci(number - 2))
n = int(input())
print(Fibonacci(n))