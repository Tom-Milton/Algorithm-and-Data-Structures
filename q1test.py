#q1test.py
#algorithms and data structures assignment 2019-20 q1
#matthew johnson 22 november 2019

#####################################################

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

def test_hq():
    assert hash_quartic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == [4, 10, 16, 22, 5, 11, 17, 23, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21]
    assert hash_quartic([19,38,57,76,95,114,133,152,171,190]) == ['-', 171, '-', 114, '-', 57, '-', '-', 190, '-', 133, '-', 76, '-', 19, '-', '-', 152, '-', 95, '-', 38, '-']
    assert hash_quartic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [71, 53, 59, 73, 5, 11, 17, 23, 29, 79, 41, 47, 7, 13, 19, 2, 31, 37, 43, 3, '-', 61, 67]
    print ("all tests passed")

def test_dh():
    assert hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == [4, 10, 16, 22, 5, 11, 17, 23, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21]
    assert hash_double([19,38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323,342,361]) == ['-', 171, 361, 114, 304, 57, 247, '-', 190, '-', 133, 323, 76, 266, 19, 209, '-', 152, 342, 95, 285, 38, 228]
    assert hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [67, 73, 79, 53, 5, 11, 17, 23, 29, '-', 41, 47, 7, 13, 19, 2, 31, 37, 43, 3, 71, 61, 59]
    print ("all tests passed")

test_hq()
test_dh()
