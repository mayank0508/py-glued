#print kth alphabet
k = int(input())
x = ord('A')
getChar = x + k - 1
printChar = chr(getChar)
print(printChar)

# this above method is used to generate Alphabet from numbers

############################################################################################################

n = int(input())
i = 1
while(i<=n):
    j = 1
    while(j<=n):
        CharP = chr(ord('A') + j - 1)
        print(CharP, end='')
        j = j + 1
    print()
    i = i + 1