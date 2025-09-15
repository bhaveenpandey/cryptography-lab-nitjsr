# Roll No: 2025PGCSIS18
# Polynomial arithmetic under GF(2P)
# Addition Modulo


# Addition Modulo
def additionModulo(p1, p2):
    maxLen = max(len(p1), len(p2))
    p1 = [0] * (maxLen - len(p1)) + p1
    p2 = [0] * (maxLen - len(p2)) + p2
    return list(map(lambda x, y : x ^ y, p1, p2))


if __name__ == "__main__":    
    A = [1, 0, 1, 1]
    B = [1, 1, 1, 0, 0]
    print(additionModulo(A, B))
