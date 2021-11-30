num = int(input())
rev = 0
while(num != 0):
    curr_rev = num%10
    num = num//10
    rev = rev*10 + curr_rev
print(rev)