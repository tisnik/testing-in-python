"""Implementace naivního algoritmu bublinkového řazení."""


def bubble_sort(alist):
    """Implementace naivního algoritmu bublinkového řazení."""
    cnt = len(alist)*(len(alist)-1)/2
    for i in range(len(alist)-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
            cnt -= 1
            if cnt == 0:
                return alist
    return alist


if __name__ == '__main__':
    print(bubble_sort([]))
    print(bubble_sort([1]))

    print(bubble_sort([1, 2]))
    print(bubble_sort([2, 1]))

    print(bubble_sort([1, 2, 3, 4]))
    print(bubble_sort([1, 2, 4, 3]))
    print(bubble_sort([1, 4, 3, 2]))
    print(bubble_sort([4, 3, 2, 1]))

    print(bubble_sort([1, 5, 4, 3, 2]))
    print(bubble_sort([5, 4, 3, 2, 1]))
