def partition(a, start, end):
    pivot = a[(start + end) // 2]
    i = start
    j = end
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return i
def qSort(a, start, end):
    if start < end:
        temp = partition(a, start, end)
        qSort(a, start, temp - 1)
        qSort(a, temp, end)

a = [1,5,3,4,6]
print(a)
qSort(a, 0, len(a) - 1)
print(a)