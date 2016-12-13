def transpose(arr):
    ans =  zip(*arr)
    return [list(i) for i in ans]
