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