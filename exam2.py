import random
import time

# Employee record structure
class Employee:
    def __init__(self, name: str, emp_id: int, salary: float):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name}, id={self.emp_id}, salary={self.salary:.2f})"


# Merge Sort by salary descending
def merge_sort_employees(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_employees(arr[:mid])
    right = merge_sort_employees(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].salary > right[j].salary:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Quick Sort by salary descending
def quick_sort_employees(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].salary
    greater = [x for x in arr if x.salary > pivot]
    equal = [x for x in arr if x.salary == pivot]
    less = [x for x in arr if x.salary < pivot]
    return quick_sort_employees(greater) + equal + quick_sort_employees(less)


def top_n_employees(sorted_arr, n=5):
    return sorted_arr[:n]


def measure_runtime(sort_func, arr):
    work = arr.copy()
    start = time.perf_counter()
    sort_func(work)
    end = time.perf_counter()
    return end - start


def main():
    employees = [
        Employee("Alice", 101, 76000),
        Employee("Bob", 102, 51000),
        Employee("Carol", 103, 92000),
        Employee("David", 104, 84000),
        Employee("Eva", 105, 60000),
        Employee("Frank", 106, 72000),
        Employee("Grace", 107, 98000),
        Employee("Heidi", 108, 66000),
        Employee("Ivan", 109, 58000),
        Employee("Judy", 110, 81000),
    ]

    print("Original employees:")
    for e in employees:
        print(e)

    sorted_merge = merge_sort_employees(employees)
    sorted_quick = quick_sort_employees(employees)

    print("\nTop 5 highest paid (Merge Sort):")
    for e in top_n_employees(sorted_merge, 5):
        print(e)

    print("\nTop 5 highest paid (Quick Sort):")
    for e in top_n_employees(sorted_quick, 5):
        print(e)

    # Larger dataset runtime comparison
    large_count = 100000
    random_employees = [
        Employee(f"Emp{i}", i, random.uniform(30000, 200000))
        for i in range(large_count)
    ]

    t_merge = measure_runtime(merge_sort_employees, random_employees)
    t_quick = measure_runtime(quick_sort_employees, random_employees)

    print(f"\nRuntime for {large_count} records:")
    print(f"  Merge Sort: {t_merge:.6f} seconds")
    print(f"  Quick Sort: {t_quick:.6f} seconds")

    if t_merge < t_quick:
        print("  Merge Sort was faster for this dataset.")
    elif t_quick < t_merge:
        print("  Quick Sort was faster for this dataset.")
    else:
        print("  Both algorithms had similar runtime.")

if __name__ == "__main__":
    main()
