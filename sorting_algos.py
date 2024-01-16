def main():
    print(sorting([9,8,7,6,4,5,4,3,2,1,0]))


def bubblesort(a_list, j=0):
    count = 0
    for i in range(len(a_list) - j - 1):
        if a_list[i] > a_list[i + 1]:
             tmp = a_list[i]
             a_list[i] = a_list[i + 1]
             a_list[i + 1] = tmp
             count += 1
    j += 1
    if not count:
        return a_list
    else:
        return bubblesort(a_list, j)

def sorting(a_list):
    for i in range(len(a_list)):
         for j in range(i + 1, len(a_list)):
            if a_list[i] < a_list[j]:
                tmp = a_list[i]
                a_list[i] = a_list[j]
                a_list[j] = tmp

    return a_list

def removal_sort(a_list, sorted_list = None):
    if sorted_list is None:
        sorted_list = []
    if len(a_list) == 0:
        return sorted_list
    else:
        sorted_list.append(min(a_list))
        a_list.remove(min(a_list))
        return removal_sort(a_list, sorted_list)

def binary_search(a_list,target):
    if target not in a_list:
        return f"not found"

    left, right = a_list[0:len(a_list)//2], a_list[len(a_list)//2 + 1:]

    if target in left:
        return f"Found in left half"
    elif target in right:
        return f"Found in right half"

    if target > left[len(left) - 1]:
        return binary_search(right,target)
    elif target < right[0]:
        return binary_search(left,target)

def fact(num):
    if num == 0: return 1
    else: return num * fact(num - 1)

def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_index = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[min_index] > unsorted_list[j]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    return unsorted_list


def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

    return unsorted_list


def merge_recursive(list_1, list_2, merged_list=None):
    if not merged_list:
        merged_list = []

    if not list_1:
        merged_list.extend(list_2)
        return merged_list
    elif not list_2:
        merged_list.extend(list_1)
        return merged_list

    if list_1[0] < list_2[0]:
        merged_list.append(list_1[0])
        list_1.pop(0)
        return merge_recursive(list_1, list_2, merged_list)

    elif list_1[0] > list_2[0]:
        merged_list.append(list_2[0])
        list_2.pop(0)
        return merge_recursive(list_1, list_2, merged_list)


def merge_iterative(list1, list2):
    merged_list = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1[0])
            list1.pop(0)
        elif list1[0] > list2[0]:
            merged_list.append(list2[0])
            list2.pop(0)
    else:
        merged_list.extend(list1)
        merged_list.extend(list2)

    return merged_list

def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    left = unsorted_list[:len(unsorted_list)//2]
    right = unsorted_list[len(unsorted_list)//2:]


    return merge_iterative(merge_sort(left), merge_sort(right))



if __name__ == "__main__":
    main()