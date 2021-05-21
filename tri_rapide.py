def placerPivot(l, first, last, pivot):
    i = first
    j = last
    while i <= j:
        while (i <= j) and (l[i] <= l[pivot]):
            i += 1
        while (i <= j) and (l[j] > l[pivot]):
            j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
    l[first], l[j] = l[j], l[first]
    return j


def triRapideRec(l, first, last):
    if first < last:
        pivot = placerPivot(l, first, last, first)
        triRapideRec(l, first, pivot - 1)
        triRapideRec(l, pivot + 1, last)


def triRapide(l):
    triRapideRec(l, 0, len(l) - 1)


maListe = [i for i in range(20, 0, -1)]
print(maListe)
triRapide(maListe)
print(maListe)