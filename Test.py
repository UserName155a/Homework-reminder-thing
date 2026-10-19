def quicksort_times(arr):
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Standard string comparisons work perfectly because "02:15" < "11:30"
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_times(left) + middle + quicksort_times(right)

# Example usage:
time_data = ["14:30", "02:15", "00:05", "23:59", "02:00", "12:00"]
print("Sorted Times:", quicksort_times(time_data))
# Output: ['00:05', '02:15', '02:00', '12:00', '14:30', '23:59']
