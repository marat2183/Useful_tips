def merge(a, b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


def merge_sorti(a):
    if len(a) > 1:
        first = a[: len(a) // 2]
        second = a[len(a) // 2:]
        third = merge_sorti(first)
        fourth = merge_sorti(second)
        return merge(third, fourth)
    else:
        return a

a = [8,9,0,1,3,2,4]
print(merge_sorti(a))