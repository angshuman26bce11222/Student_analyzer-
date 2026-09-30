def compute_summation(numbers: list) -> float:
    """Manual implementation of summation algorithm."""
    total = 0.0
    for num in numbers:
        total += num
    return total

def find_maximum_score(students: list) -> dict:
    """Finds the student record with the maximum total score."""
    if not students:
        return None
    
    max_student = students[0]
    for student in students[1:]:
        if student["total"] > max_student["total"]:
            max_student = student
    return max_student

def partition(arr: list, low: int, high: int) -> int:
    """Partitions array around a pivot for quickselect / sorting."""
    pivot = arr[high]["total"]
    i = low - 1
    for j in range(low, high):
        if arr[j]["total"] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def find_kth_smallest(students: list, k: int) -> dict:
    """Finds the K-th lowest performing student using partitioning concept."""
    if not (1 <= k <= len(students)):
        return None
    
    arr_copy = list(students)
    
    def quickselect(low, high, target_k):
        if low <= high:
            pi = partition(arr_copy, low, high)
            if pi == target_k:
                return arr_copy[pi]
            elif pi > target_k:
                return quickselect(low, pi - 1, target_k)
            else:
                return quickselect(pi + 1, high, target_k)
        return None

    return quickselect(0, len(arr_copy) - 1, k - 1)