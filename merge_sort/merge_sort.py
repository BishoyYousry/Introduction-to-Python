def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point of the array
        mid = len(arr) // 2
        
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively split the array until each subarray has one element
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the two halves
        i = j = k = 0
        
        # Merge the left and right halves back into the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any element was left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check if any element was left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", merge_sort(arr))