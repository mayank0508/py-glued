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
    
    
choice = int(input())
while choice!=6:
    if choice<=5 and choice>=1:
        num1 = int(input())
        num2 = int(input())
        
    if choice ==1:
        print(num1 + num2)
    
    if choice == 2:
        print(num1 - num2)

    if choice == 3:
        print(num1 * num2)

    if choice == 4:  
        print(num1 // num2)

    if choice == 5:
        print(num1 % num2)
    
    if choice >= 7:
        print("Invalid Operation")
     
    choice = int(input()) # this is the most imp part of the question