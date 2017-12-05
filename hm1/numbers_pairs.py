def print_pairs(sum, *args):
    k = 0
    n = args.__len__()

    list_of_pairs = [None] * n

    for i in args:
        list_of_pairs[k] = i
        k += 1

    l=0
    m=l+1

    for l in range(n-1):
            for m in range(n):
                if(list_of_pairs[l] + list_of_pairs[m] == 10):
                    print(list_of_pairs[l], list_of_pairs[m])

#Example
# print_pairs(10, 7,3,1,2,9,1)
# Duplicates removing have not implemented yet
