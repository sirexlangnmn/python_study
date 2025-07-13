def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize: stop if no swap happened
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if they're in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Array is already sorted
    return arr


# Example
scores = [75, 89, 92, 67, 45, 58]
sorted_scores = bubble_sort(scores)
print("Sorted scores:", sorted_scores)
