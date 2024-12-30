def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted into the sorted part of the array
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into the correct position
        arr[j + 1] = key
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", insertion_sort(arr))
