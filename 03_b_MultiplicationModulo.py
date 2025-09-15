#  Roll No: 2025PGCSIS18

# Polynomial arithmetic under GF(2P)
# a) Addition Modulo
# b) Multiplication Modulo
# c) Multiplication Modulo (computational efficient approach)

# Multiplication Modulo
# def additionModulo(p1, p2):
#     maxLen = max(len(p1), len(p2))
#     p1 = [0] * (maxLen - len(p1)) + p1
#     p2 = [0] * (maxLen - len(p2)) + p2
#     return list(map(lambda x, y : x ^ y, p1, p2))

# def shift(p):
#     for i in range(0, len(p) - 1):
#         p[i] = p[i+1]

#     p[len(p)-1] = 0
    
#     return p

# def multiplicationModulo(fx, gx, mx):
#     result = [0] * len(fx)

#     for i , j in enumerate(gx[::-1]):
#         z = fx[0]
        
#         if(i != 0):
#             fx = shift(fx)

#         if(z == 1):
#             fx = list(map(lambda x, y : x ^ y, fx, mx))

#         if(j == 1):
#             result = additionModulo(result, fx)

#     return result

# if __name__ == "__main__":
#     fx = [0,1,0,1,0,1,1,1]
#     gx = [1,0,0,0,0,0,1,1]
#     mx = [0,0,0,1,1,0,1,1]
#     # ans = [1,1,0,0,0,0,0,1]
#     # print(multiplicationModulo(fx, gx, mx) == ans)
#     print(multiplicationModulo(fx, gx, mx))

# def GF(A , B):
#     max1 = max(len(A) , len(B))
#     A = [0] * (max1 - len(A)) + A
#     B = [0] * (max1 - len(B)) + B
#     return list(map(lambda x , y : x ^ y , A , B ))

# A = [1,0,1,1]
# B = [1,0,1,1,1,0,1,1]

A = [1, 0, 0, 0, 0, 0, 1, 1]
B = [0, 1, 0, 1, 0, 1, 1, 1]

ans = [0] * (len(A) + len(B))

for i in range(0, len(A)):
    idx_a = len(A) - i - 1
    for j in range(0, len(B)):
        idx_b = len(B) - j - 1
        if(A[idx_a] == 1 and B[idx_b] == 1):
            ans[idx_a + idx_b] += 1

for i in range(len(ans)):
    if(ans[i] % 2 == 0):
        ans[i] = 0
    else:
        ans[i] = 1
print(ans[:-1])
