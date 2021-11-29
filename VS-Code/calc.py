# # Write your code here
# op = int(input())
# while(5>= op):
#     n = int(input())
#     m = int(input())


# if(op == 1):
#     print(n+m)
# elif(op == 2):
#     print(n-m)
# elif(op == 3):
#     print(n*m)
# elif(op == 4):
#     print(n//5)
# elif(op == 5):
#     print(n%m)

# if(op == 7):
#     print("Invalid Operation")
    
    
n = int(input())

while n!=6:


    if n<=5 and n>=1:
        num1 = int(input())
        num2 = int(input())
        
    if n ==1:
        print(num1 + num2)
    
    if n == 2:
        print(num1 - num2)

    if n == 3:
        print(num1 * num2)

    if n == 4:  
        print(num1 // num2)

    if n == 5:
        print(num1 % num2)
    
    elif 1 > n or n > 6:
        print("Invalid Operation")
     
    n = int(input())