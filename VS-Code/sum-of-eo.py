
n = int(input())
sum_e = 0
sum_o = 0

while(n != 0):
    reg = n%10
    if(reg%2 == 0):
        sum_e = sum_e + reg
    else:
        sum_o = sum_o + reg
    n = n//10

print(sum_e,' ',sum_o)
