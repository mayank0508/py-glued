# Read input as sepcified in the question
# Print output as specified in the question

S = int(input())
E = int(input())
W = int(input())

while(E >= S):
    C = (S-32) * 5/9
    M = int(C)
    print(S,"\t",M)
    S = S + W
