# # Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]

# # Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']

# words = ["apple", "bat", "cherry", "dog", "elderberry"]

# out = [a.upper() for a in words]
# out = out[::2]
# print(out)


# # Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}

# # Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}

# dict_a = {'a': 10, 'b': 20} 
# dct_b = {'b': 5, 'c': 15}
# merged = dict_a.copy()

# for key, value in dct_b.items():
#     if key in merged:
#         merged[key] = value + merged[key]
#     else:
#         merged[key] = value

# print(merged)


# # Given Input: text = "Python Programming"

# # Expected Output:
# # Character Frequency: 
# # Counter({'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'a': 1, 'g': 2, 'm': 2, 'i': 1})

# from collections import Counter

# text = "Python Programming"

# text = text.lower().replace(" ", "")

# print(f"Character Frequency: \n{Counter(text)}")


# # Given Input: word1 = "listen", word2 = "silent"

# # Expected Output: Is "listen" an anagram of "silent"? True

# word1 = input("Enter a word ")
# word2 = input("Enter another word for anagram check ")

# print(f"Is \"{word2}\" and anagram of \"{word1}\"? {"".join(sorted(word1)) == "".join(sorted(word2))}")


# # Given Input: nested = [1, [2, 3], [4, [5, 6]], 7]

# # Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]

# nested = [1, [2, 3], [4, [5, 6]], 7]

# def flatten(nested_list):
#     out = []
#     for i in nested_list:
#         if type(i) == list:
#             out.extend(flatten(i))
#         else:
#             out.append(i)
#     return out

# print(flatten(nested))


# # Given Input: "Python is awesome"

# # Expected Output: "nohtyP si emosewa"

# a = input("Enter a sentence: ")

# a = a.split(" ")
# a = [i[::-1] for i in a]
# a = " ".join(a)

# print(a)


# # Palindrome Sentence 
# # Given Input: "A man, a plan, a canal: Panama"

# # Expected Output: True

# a = input("Enter a sentence: ")

# sanitized = ''

# for i in a:
#     if i.isalnum():
#         sanitized += i.lower()

# rev = sanitized[::-1]

# print(rev == sanitized)


# # must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).
# # Given Input: ["apple", "education", "ice", "ocean", "python", "umbrella"]

# # Expected Output: ['education', 'umbrella']

# o = ["apple", "education", "ice", "ocean", "python", "umbrella"]

# o = [i for i in o if i[0].lower() in ['a','e','i','o','u'] and len(i) > 5]

# print(o)


# # sequence integrity
# # Given Input: [1, 2, 2, 3, 1, 4, 2]

# # Expected Output: [1, 2, 3, 4]

# h = [1, 2, 2, 3, 1, 4, 2]

# f = []

# for i in h:
#     if i not in f:
#         f.append(i)

# print(f)


# # Given Input: List: [1, 2, 3, 4, 5], Shift: 2, Direction: 'right'

# # Expected Output: [4, 5, 1, 2, 3]

# def circular_shift(inp, shift_count, direction):
#     if direction.lower() == "right":
#         a = inp[-(shift_count):]
#         b = inp[0:-(shift_count)]
#         out = a + b
#     elif direction.lower() == "left":
#         a = inp[shift_count:]
#         b = inp[0:shift_count]
#         out = a + b
#     else:
#         out = "Return a valid rotatory direction"
#     return out

# print(circular_shift([1, 2, 3, 4, 5], 2, 'left'))


# # Given Input: d1 = {"a": 1, "b": 2}, d2 = {"b": 3, "c": 4}

# # Expected Output: {'a': [1], 'b': [2, 3], 'c': [4]}

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# merged = d1.copy()

# for key, value in d2.items():
#     if key in merged:
#         merged[key] = [value, merged[key]]
#     else:
#         merged[key] = value

# print(merged)


# # Given Input: {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

# # Expected Output: {'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}

# d = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

# new = {}

# for key, value in d.items():
#     for v in value:
#         new[v] = key

# print(new)


# # Given Input: employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]

# # Expected Output: [{'name': 'B', 'salary': 70}, {'name': 'C', 'salary': 60}, {'name': 'A', 'salary': 50}]

# inp = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]

# out = sorted(inp, key=lambda x: x['salary'], reverse=True)

# print(out)


# # Given Input: Set A: {1, 2, 3}, Set B: {1, 2, 3, 4, 5} (Find subset, superset, disjoint)

# # Expected Output: Set A is a subset of Set B.

# A = {1, 2, 3}
# B = {1, 4, 5}

# if A.issubset(B):
#     print("A is a subset of B")
# elif B.issubset(A):
#     print("B is a subset of A")
# elif A.isdisjoint(B):
#     print("Both sets are disjoint(Share no elements)")
# else:
#     print("Common elements in the sets are", A & B)


# # Given Input: list1 = [101, 102, 103], list2 = [103, 104, 105]

# # Expected Output: {101, 102, 104, 105}

# list1 = [101, 102, 103]
# list2 = [103, 104, 105]

# print(set(list1) ^ set(list2))


# # Power Set Generation Given Input: [1, 2, 3]

# # Expected Output: [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

# from itertools import combinations

# def get_power_set(s):
#     elements = list(s)
#     power_set = []
    
#     for r in range(len(elements) + 1):
#         for combo in combinations(elements, r):
#             power_set.append(combo)
#             print(combo)
#         print(r)
#     return power_set

# my_set = {1, 2, 3}
# print(f"Power Set: {get_power_set(my_set)}")


# # Method Resolution Order in Python (MRO)

# class A:
#     def f1(self):
#         print("f1 works")
#     def f2(self):
#         print("f2 works")
#     def show(self):
#         print("In A Show")

# class B(A):
#     def f3(self):
#         print("f3 works")
#     def f4(self):
#         print("f4 works")
#     def show(self):
#         print("In B Show")

# class C(B):
#     def f5(self):
#         print("f5 works")
#     def f6(self):
#         print("f6 works")
#     # def show(self):
#     #     print("In C Show")

# obj1 = C()
# obj1.show()# Works heirarchically


# # Given Input: Birthdate: 1995-05-15, Today: 2026-01-02

# # Expected Output: Age: 30 years, 7 months, 18 days

# Birthdate = "1995-05-15"

# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# Birthdate = datetime.strptime(Birthdate, "%Y-%m-%d").date()
# out = datetime.now().date()

# out = relativedelta(out, Birthdate)

# print(f"Age of person is {out.years} years, {out.months} months, {out.days} days old.")



# # Given Input: Current Date: 2026-01-02

# # Expected Output: 363 days, 16 hours, 50 minutes until New Year!

# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# Current_Date = datetime.now()

# next_year = Current_Date.year + 1

# target = datetime(next_year, 1, 1)

# out = relativedelta(target, Current_Date)

# print(f"New Year is in {out.months} Months, {out.days} Days, {out.hours} Hours and {out.minutes} Minutes.")


# # Given Input: powers = PowerOfTwo(3)

# # Expected Output: 1 2 4 8

# class PowerOfTwo:
#     def __init__(self, max_exp):
#         self.max = max_exp
#         self.n = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n <= self.max:
#             a = 2 ** self.n
#             self.n += 1
#             return a 
#         else:
#             raise StopIteration

# for i in PowerOfTwo(4):
#     print(i, end=' ')


# # Given Input: numbers = [1, 2, 3, 2, 4, 5, 1, 6]

# # Expected Output: Duplicates found: {1, 2}

# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4]

# from collections import Counter

# out = Counter(numbers)

# out = [a for a in out if out[a] > 1]

# print(f'Duplicates found : {set(out)}')


# # Singly Linked List Implementation: 
# # Given Input: List operations: Append 10, Append 20, Append 30
# # Expected Output: 10 -> 20 -> 30 -> None

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newnode = Node(data)
#         if not self.head:
#             self.head = newnode
#             return 

#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = newnode

#     def display(self):
#         current = self.head
#         while current:
#             print(f"{current.data} -> ", end="")
#             current = current.next
#         print('None')

# ll = LinkedList()
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.display()


# # Stack Implementation LIFO 
# # Given Input: Push: "google.com", "pynative.com" | Action: Pop
# # Expected Output: Current Top: pynative.com; Popped: pynative.com; New Top: google.com

# class Stack:
#     def __init__(self):
#         self.items = []

#     def pop(self):
#         out = self.items.pop()
#         return f"Popped : {out}\nNew Top : {self.items[-1]}"

#     def push(self, n):
#         self.n = n
#         self.items.append(n)
#         return f"Current Top : {n}"

# s = Stack()
# print(s.push(22))
# print(s.push(354))
# print(s.pop())


# # Queue Implementation FIFO
# # Given Input: Enqueue: "Customer A", "Customer B" | Action: Dequeue
# # Expected Output: Serving: Customer A; Next in line: Customer B

# class Queue:
#     def __init__(self):
#         self.items = []

#     def dequeue(self):
#         out = self.items.pop()
#         return f"Serving : {out}\nNext In Line : {self.items[-1]}"

#     def enqueue(self, n):
#         self.n = n
#         self.items.insert(0, n)
#         return f"Last In Line : {n}"

# q = Queue()
# print(q.enqueue(44))
# print(q.enqueue(33))
# print(q.enqueue(22))
# print(q.dequeue())