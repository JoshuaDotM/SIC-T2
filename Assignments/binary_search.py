def binary_search():
    array=list(map(int,input("Enter the digits : ").split()))
    key=int(input("Enter the search element : "))
    array.sort()
    low=0
    high=len(array)-1
    while high >= low:
        middle = (low + high) // 2
        if array[middle] == key:
            return middle
            break
        elif key > array[middle]:
            low = middle + 1
        elif key < array[middle]:
            high = middle - 1

print(binary_search())
