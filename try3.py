# Recursive Binary Search
# Given Input: Sorted List: [10, 20, 30, 40, 50, 60], Target: 50
# Expected Output: Target found at index: 4

s_list = [10, 20, 30, 40, 50, 60]
Target = 50

def r_bin_search(input : list[int], target : int) -> int:
    first = 0
    last = len(input) - 1
    mid = ((first + last) // 2) + 1
    print(first, last, mid)
    if input[mid] == target:
        return input[mid]
    elif input[mid] > target:
        last = mid - 1
        r_bin_search(input[0:last], target)
    elif input[mid] < target:
        first = mid
        r_bin_search(input[first:], target)

print(s_list.index(r_bin_search(s_list, Target)))