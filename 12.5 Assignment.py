# def merge_sort(arr):
#     """
#     Sorts a list in ascending order using Merge Sort algorithm.

#     Time Complexity:
#         Best Case: O(n log n)
#         Average Case: O(n log n)
#         Worst Case: O(n log n)

#     Space Complexity:
#         O(n)
#     """
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# # Test Case
# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# def binary_search(arr, target):
#     """
#     Searches for a target element in a sorted list.

#     Time Complexity:
#         Best Case: O(1)
#         Average Case: O(log n)
#         Worst Case: O(log n)

#     Space Complexity:
#         O(1)
#     """
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# # Test Cases
# arr = [1, 3, 5, 7, 9, 11]
# print(binary_search(arr, 7))
# print(binary_search(arr, 4))
# def sort_appointments(appointments, key):
#     return sorted(appointments, key=lambda x: x[key])


# def search_appointment(appointments, appointment_id):
#     appointments = sorted(appointments, key=lambda x: x['appointment_id'])
#     ids = [a['appointment_id'] for a in appointments]
#     index = binary_search(ids, appointment_id)
#     return appointments[index] if index != -1 else None
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# def sort_tickets(tickets, key):
#     return sorted(tickets, key=lambda x: x[key])


# def search_ticket(tickets, ticket_id):
#     tickets = sorted(tickets, key=lambda x: x['ticket_id'])
#     ids = [t['ticket_id'] for t in tickets]
#     index = binary_search(ids, ticket_id)
#     return tickets[index] if index != -1 else None


# # -------- DATA --------
# tickets = [
#     {"ticket_id": 101, "name": "Rahul", "train": 12627, "seat": 12, "date": "2026-03-01"},
#     {"ticket_id": 105, "name": "Anjali", "train": 12711, "seat": 5, "date": "2026-02-28"},
#     {"ticket_id": 103, "name": "Kiran", "train": 12645, "seat": 20, "date": "2026-03-03"}
# ]

# # -------- SORT --------
# sorted_tickets = sort_tickets(tickets, "seat")
# print("Sorted Tickets:")
# for t in sorted_tickets:
#     print(t)

# # -------- SEARCH --------
# result = search_ticket(tickets, 103)
# print("\nSearch Result:")
# print(result)
# ---------- Binary Search ----------
# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# # ---------- Sorting ----------
# def sort_allocations(records, key):
#     return sorted(records, key=lambda x: x[key])


# # ---------- Searching ----------
# def search_allocation(records, student_id):
#     records = sorted(records, key=lambda x: x['student_id'])
#     ids = [r['student_id'] for r in records]
#     index = binary_search(ids, student_id)
#     return records[index] if index != -1 else None


# # ---------- Data ----------
# allocations = [
#     {"student_id": 201, "room": 12, "floor": 1, "date": "2026-02-01"},
#     {"student_id": 205, "room": 5, "floor": 2, "date": "2026-02-03"},
#     {"student_id": 203, "room": 20, "floor": 3, "date": "2026-02-02"}
# ]

# # Sort
# print("Sorted by Room:")
# for a in sort_allocations(allocations, "room"):
#     print(a)

# # Search
# print("\nSearch Result:")
# print(search_allocation(allocations, 203))
# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# def sort_movies(movies, key):
#     return sorted(movies, key=lambda x: x[key])


# def search_movie(movies, movie_id):
#     movies = sorted(movies, key=lambda x: x['movie_id'])
#     ids = [m['movie_id'] for m in movies]
#     index = binary_search(ids, movie_id)
#     return movies[index] if index != -1 else None


# movies = [
#     {"movie_id": 1, "title": "Leo", "genre": "Action", "rating": 8.2, "year": 2023},
#     {"movie_id": 3, "title": "RRR", "genre": "Drama", "rating": 9.0, "year": 2022},
#     {"movie_id": 2, "title": "KGF", "genre": "Action", "rating": 8.8, "year": 2021}
# ]

# print("Sorted by Rating:")
# for m in sort_movies(movies, "rating"):
#     print(m)

# print("\nSearch Movie:")
# print(search_movie(movies, 2))
# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# def sort_crops(crops, key):
#     return sorted(crops, key=lambda x: x[key])


# def search_crop(crops, crop_id):
#     crops = sorted(crops, key=lambda x: x['crop_id'])
#     ids = [c['crop_id'] for c in crops]
#     index = binary_search(ids, crop_id)
#     return crops[index] if index != -1 else None


# crops = [
#     {"crop_id": 11, "name": "Rice", "moisture": 60, "temp": 28, "yield": 4.5},
#     {"crop_id": 13, "name": "Wheat", "moisture": 45, "temp": 25, "yield": 3.8},
#     {"crop_id": 12, "name": "Corn", "moisture": 55, "temp": 30, "yield": 4.0}
# ]

# print("Sorted by Moisture:")
# for c in sort_crops(crops, "moisture"):
#     print(c)

# print("\nSearch Crop:")
# print(search_crop(crops, 12))
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def sort_flights(flights, key):
    return sorted(flights, key=lambda x: x[key])


def search_flight(flights, flight_id):
    flights = sorted(flights, key=lambda x: x['flight_id'])
    ids = [f['flight_id'] for f in flights]
    index = binary_search(ids, flight_id)
    return flights[index] if index != -1 else None


flights = [
    {"flight_id": 501, "airline": "IndiGo", "departure": "10:30", "arrival": "12:00", "status": "On Time"},
    {"flight_id": 503, "airline": "Air India", "departure": "08:00", "arrival": "10:15", "status": "Delayed"},
    {"flight_id": 502, "airline": "SpiceJet", "departure": "14:00", "arrival": "16:10", "status": "Boarding"}
]

print("Sorted by Departure Time:")
for f in sort_flights(flights, "departure"):
    print(f)

print("\nSearch Flight:")
print(search_flight(flights, 502))