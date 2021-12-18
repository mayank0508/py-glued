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

########################################################################

# def checkPalindrome(num):
#     rev = 0
#     while(num != 0):
#         curr_rev = num%10
#         num = num//10
#         rev = rev*10 + curr_rev
#         pass
		
# num = int(input())
# rev = num
# if(rev):
#  	print('true')
# else:
#  	print('false')

################################################################


# Changed num variable to string, 
# and calculated the length (number of digits)

# initialize sum
# def Arm(num):
#     order = len(str(num))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     pass

# # display the result
# num = int(input())
# if num == sum:
#    print('true')
# else:
#    print('false')

# def power(x, y):
      
#     if y == 0:
#         return 1
#     if y % 2 == 0:
#         return power(x, y // 2) * power(x, y // 2)
          
#     return x * power(x, y // 2) * power(x, y // 2)
  
# # Function to calculate order of the number
# def order(x):
  
#     # Variable to store of the number
#     n = 0
#     while (x != 0):
#         n = n + 1
#         x = x // 10
          
#     return n

# def isArmstrong(x):
      
#     n = order(x)
#     temp = x
#     sum1 = 0
      
#     while (temp != 0):
#         r = temp % 10
#         sum1 = sum1 + power(r, n)
#         temp = temp // 10
  
#     # If condition satisfies
#     return (sum1 == x)

################################################################

def armstrong(n):
    number = str(n)
 
    n = len(number)
    output = 0
    for i in number:
      output = output+int(i)**n
 
    if output == int(number):
        print('true')
    else:
        print('false')
         
n = int(input())
armstrong(n)

#################################################

# def checkPalindrome(num):
#     rev = 0
#     while(num != 0):
#         curr_rev = num%10
#         num = num//10
#         rev = rev*10 + curr_rev
        
#     rev = num
#     if(rev):
#         print('true')
#     else:
#         print('false')
#     pass
		
# num = int(input())
# checkPalindrome(num)

def checkPalindrome(num):
    temp = num
    rev = 0
    
    while temp != 0:
        rev = (rev*10) + (temp % 10)
        temp = temp // 10
        
    if num == rev :
        return True
    else:
        return False
    

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
