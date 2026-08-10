# # Recursive Binary Search
# # Given Input: Sorted List: [10, 20, 30, 40, 50, 60], Target: 50
# # Expected Output: Target found at index: 4

# s_list = [10, 20, 30, 40, 50, 60]
# Target = 50

# def bin_search(sorted : list[int], target : int, start : int = 0, end : int = None) -> int:
#     if end is None:
#         end = len(sorted) - 1
#     if start > end:
#         return - 1
#     mid = (start + end) // 2
#     if sorted[mid] == target:
#         return mid
#     elif sorted[mid] > target:
#         return bin_search(sorted, target, start, mid - 1)
#     else:
#         return bin_search(sorted, target, mid + 1, end)

# print(f"Target found at index: {bin_search(s_list, Target)}")


# # Given Input: employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]
# # Expected Output: [('Bob', 25, 75000), ('Charlie', 35, 60000), ('Alice', 30, 50000)]

# employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]

# employees = sorted(employees, key = lambda a : a[2], reverse = True)

# print(employees)


# # Map and Filter Combination
# # Given Input: nums = [1, 2, 3, 4, 5, 6]
# # Expected Output: [4, 16, 36]

# nums = [1, 2, 3, 4, 5, 6]

# nums = filter(lambda a : a % 2 == 0, nums)
# nums = list(map(lambda s : s ** 2, nums))

# print(nums)


# # @timer decorator

# import time

# def timer(func):
#     def wrapper(*args):
#         start_time = time.perf_counter() # High-precision start
#         result = func(*args)   # Run the actual function
#         end_time = time.perf_counter()   # High-precision end
        
#         duration = end_time - start_time
#         print(f"Function '{func.__name__}' took {duration:.4f} seconds.")
#         return result
#     return wrapper

# @timer
# def lol(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     time.sleep(3)
#     return [a, b]

# print(lol(4, 5))


# # Fibonacci Generator (Memory Efficiency) using yield keyword
# # Given Input: n = 8
# # Expected Output: First 8 Fibonacci numbers: 0 1 1 2 3 5 8 13 

# def fib(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1

# for i in fib(8):
#     print(i)


# # Custom Context Manager (with statement)
# # Given Input: A block of code inside a with statement that might raise an Exception.
# # Expected Output:
# # Connecting to Database... Processing data... 
# # Error: something went wrong 
# # Closing Database Connection safely.

# class Database:
#     def __enter__(self):
#         print("Connecting to Database... Processing data...")
#         return self

#     def __exit__(self, exc_type, exc, tb):
#         print("Error: something went wrong \nClosing Database Connection safely.")
#         return False

# try:
#     with Database() as db:
#         raise ConnectionError
# except:
#     pass


# # Given Input: log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
# # Expected Output: Event: User Login; Details: ('admin', 'dashboard'); Metadata: {'timestamp': '10:00 AM', 'status': 'Success'}

# def logger(event, *args, **kwargs):
#     return f"Event: {event}, Details: {args}, Metadata: {kwargs}"

# print(logger("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success"))


# # Zip and Enumerate Mapping
# # Given Input: names = ["Alice", "Bob", "Charlie"]; scores = [85, 92, 78]
# # Expected Output: Rank 1: Bob scored 92; Rank 2: Alice scored 85; Rank 3: Charlie scored 78

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# out = list(zip(names, scores))

# out = sorted(out, key = lambda x : x[1], reverse = True)

# for i, (names, scores) in enumerate(out):
#     print(f"Rank {i+1}: {names} scored {scores}")


# # Memoization using lru_cache
# # Given Input: fibonacci(50)
# # Expected Output: 12586269025

# from functools import lru_cache
# import time

# def timer(func):
#     def wrapper(*args):
#         start_time = time.perf_counter() # High-precision start
#         result = func(*args)   # Run the actual function
#         end_time = time.perf_counter()   # High-precision end
        
#         duration = end_time - start_time
#         print(f"Function '{func.__name__}' took {duration:.8f} seconds.")
#         return result
#     return wrapper

# @timer
# @lru_cache(maxsize=None)
# def fib(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         a, b = b, a + b
#         count += 1
#     return a

# @timer
# def fib_wo_cache(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         a, b = b, a + b
#         count += 1
#     return a

# print(fib_wo_cache(50))
# print(fib(50))


# # Set Operations for Data Analysis
# # Given Input: trial = [1, 2, 3, 4, 5]; paid = [4, 5, 6, 7, 8]
# # Expected Output: Upgraded (Both): {4, 5}; Leads (Trial only): {1, 2, 3}; Unique Status (Not both): {1, 2, 3, 6, 7, 8}

# trial = [1, 2, 3, 4, 5]; paid = [4, 5, 6, 7, 8]
# trial = set(trial); paid = set(paid)
# print(f"Upgraded (Both): {trial & paid}")
# print(f"Leads (Trial only): {trial - paid}")
# print(f"Unique Status (Not Both): {trial ^ paid}")


