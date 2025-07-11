def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index
    return -1  # Not found


# Example 1
students = ["Ana", "Ben", "Carla", "Dino", "Ella"]
target_name = "Carla"


# Example 2
scores = [75, 89, 92, 67, 45, 58]
target_score = 92


result = linear_search(students, target_name)
result2 = linear_search(scores, target_score)


if result != -1:
    print(f"{target_name} found at index {result}")
else:
    print(f"{target_name} not found")

if result2 != -1:
    print(f"{target_score} found at index {result2}")
else:
    print(f"{target_score} not found")