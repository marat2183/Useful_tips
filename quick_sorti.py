def quick_sort(a):
    if len(a) > 1:
        x = a[0]
        left = [i for i in a if i < x]
        mid = [i for i in a if i == x]
        right = [i for i in a if i > x]
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return a

test = [9, 0, 12, 39, 41, 41, 43, 3, 1]
print(quick_sort(test))