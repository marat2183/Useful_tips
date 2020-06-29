def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()
    low_el = []
    high_el = []
    for el in a:
        if el < pivot:
            low_el.append(el)
        else:
            high_el.append(el)

    return quick_sort(low_el) + [pivot] + quick_sort(high_el)

a = [-5,1,2,3,5,6,2]
print(quick_sort(a))