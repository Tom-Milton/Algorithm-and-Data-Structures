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