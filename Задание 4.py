def max_in(lis):
    if lis[0] == max(lis):
        return 1
    else:
        return 1 + max_in(lis[1:])
print(max_in([1,54,57,2]))
