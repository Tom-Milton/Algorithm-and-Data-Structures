#q2test.py
#algorithms and data structures assignment 2019-20 q2
#matthew johnson 22 november 2019

#####################################################

def descendants(n1, n2, k):
    numbers_so_far = {} #dictionary containing sequences of descendants for all previous numbers
    equal_to_k = []
    for i in range(1, n2): #(mostly) quicker to check between 1 and n2 rather than n1 and n2
        previous_descendants = []
        descendant = sum(factorial(int(j)) for j in str(i)) #generates next descendant
        while descendant not in previous_descendants: #keeps adding descendants to list until one reoccurs
            if 1 <= descendant < i and descendant not in numbers_so_far[descendant]: #adds sequence of descendants from dictionary
                previous_descendants.append(descendant)
                previous_descendants.extend(numbers_so_far[descendant])
                break
            else:
                previous_descendants.append(descendant)
                descendant = sum(factorial(int(j)) for j in str(descendant))
        numbers_so_far[i] = previous_descendants
        if len(previous_descendants) == k and n1 <= i < n2:
            equal_to_k.append(i)
    return len(equal_to_k)

def factorial(n):
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880] #only factorials of first 10 digits required
    return fact[n]

def q2test():
    assert descendants(1,2,1) == 1
    assert descendants(1,200,1) == 6
    assert descendants(1,200,2) == 2
    assert descendants(1,2000,3) == 33
    assert descendants(4000,6000,3) == 36
    assert descendants(123456,654321,20) == 4015
    assert descendants(1,1000000,59) == 402
    assert descendants(1,1000000,60) == 0
    print ("all tests passed")
    
q2test()
