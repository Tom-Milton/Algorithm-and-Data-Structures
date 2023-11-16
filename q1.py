def hash_quartic(d):
    table = ["-"]*23 #intialises table
    for k in d:
        if k in table: #can't have same key twice
            continue
        i = (4*k + 7) % 23
        count = 0
        j = 1
        while table[i] != "-": #keeps finding new bucket until empty one is found
            i = ((4*k + 7) % 23 + j**4) % 23 #quartic probing function
            count += 1
            j += 1
            if count == 22:
                return table
        table[i] = k
    return table


def hash_double(d):
    table = ["-"]*23
    for k in d:
        if k in table:
            continue
        i = (4*k + 7) % 23
        h = 17 - (k % 17) #secondary hash function
        count = 0
        j = 1
        while table[i] != "-":
            i = ((4*k + 7) % 23 + j*h) % 23
            count += 1
            j += 1
            if count == 22:
                return table
        table[i] = k
    return table