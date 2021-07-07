def deep_reverse(L):
    result = []
    for i in L:
        result.append(i[::-1])
    L[:] = result[::-1]
    return L
L=[[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
