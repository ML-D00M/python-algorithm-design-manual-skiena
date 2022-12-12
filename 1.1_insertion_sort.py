def insertion_sort (arr):
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j - 1
    return arr

def main():
    arr1 = [154, 245, 568, 324, 654, 324]
    arr2 = ['Mike', 'Bob', 'Sally', 'Jil', 'Jan']
    print(insertion_sort (arr1))
    print(insertion_sort (arr2))

main()