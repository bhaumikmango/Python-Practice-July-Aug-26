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


