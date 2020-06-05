def insert_sort(A):
    N = len(A)
    for i in range(1,N):
        k = i
        while k > 0 and A[k-1] > A[k]:
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1
    print(A)
