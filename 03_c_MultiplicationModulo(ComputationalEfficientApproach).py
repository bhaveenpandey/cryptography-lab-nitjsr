# Roll No: 2025PGCSIS18
# Polynomial arithmetic under GF(2P)
# a) Addition Modulo
# b) Multiplication Modulo
# c) Multiplication Modulo (computational efficient approach)

# Multiplication Modulo (computational efficient approach)
def additionModulo(p1, p2):
    maxLen = max(len(p1), len(p2))
    p1 = [0] * (maxLen - len(p1)) + p1
    p2 = [0] * (maxLen - len(p2)) + p2
    return list(map(lambda x, y : x ^ y, p1, p2))

def shift(p):
    for i in range(0, len(p) - 1):
        p[i] = p[i+1]

    p[len(p)-1] = 0
    
    return p

def multiplicationModulo(fx, gx, mx):
    result = [0] * len(fx)

    for i , j in enumerate(gx[::-1]):
        z = fx[0]
        
        if(i != 0):
            fx = shift(fx)

        if(z == 1):
            fx = list(map(lambda x, y : x ^ y, fx, mx))

        if(j == 1):
            result = additionModulo(result, fx)

    return result

if __name__ == "__main__":
    fx = [0,1,0,1,0,1,1,1]
    gx = [1,0,0,0,0,0,1,1]
    mx = [0,0,0,1,1,0,1,1]
    # ans = [1,1,0,0,0,0,0,1]
    # print(multiplicationModulo(fx, gx, mx) == ans)
    print(multiplicationModulo(fx, gx, mx))
