def choice_sort(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                A[j], A[i] = A[i], A[j]
    print(A)


choice_sort([5,3,4,1])