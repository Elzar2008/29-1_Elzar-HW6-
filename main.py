def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def binary_search(item, lst):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if found:
        print(f"{item} найден в списке.")
    else:
        print(f"{item} не найден в списке.")

unsorted_lst = [5, 3, 8, 6, 7, 2]
sorted_lst = bubble_sort(unsorted_lst)
print(sorted_lst)

item = 6
binary_search(item, sorted_lst)





