#Challenge 48: Binary Search
def binary_search(arr, n):
    arr.sort()
    s, e = 0, len(arr)-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == n: 
            return mid
        elif arr[mid] < n:
            s = mid + 1
        elif arr[mid] > n:
            e = mid - 1
    return -1 #not in list


list1 = [12, 34, 56, 78, 98, 22, 45, 13]
print(binary_search(list1, 22))
print(binary_search(list1, 15))
