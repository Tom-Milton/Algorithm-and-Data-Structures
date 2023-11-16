import sys

#py kWayQS.py 1000 Sample.txt

def read_input(filename):
    A = []
    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A


def insertionsort(A):
    for i in range(1, len(A)):
        j = i
        temp = A[j]
        while j > 0 and temp < A[j - 1]:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = temp
    return A


def quicksort(A, k):
    if len(A) <= 2*k:
        return insertionsort(A)
    else:
        pivots = insertionsort(A[:k]) #sorts pivots
        lists = [[] for _ in range(k + 1)] #initialises lists between pivots
        for i in A[k:]: #adds values to arrays between pivots
            for c, v in enumerate(pivots): #compares values against pivots
                if i < v:
                    lists[c].append(i)
                    break
            else:
                lists[-1].append(i)
        return sum([quicksort(lists[j], k) + [pivots[j]] for j in range(len(lists)-1)] + [quicksort(lists[-1], k)], [])

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A, k))
    
if __name__ == "__main__":
    main()