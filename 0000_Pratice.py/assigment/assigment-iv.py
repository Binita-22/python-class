# Write a program that prints numbers from 1 to 50.
#  For multiples of 3, print "Fizz"; for multiples
#  of 5, print "Buzz"; for multiples of both, print
# "FizzBuzz". Additionally, if the number is even, append
# "Even" to the output (e.g., 15 should print "FizzBuzzEven"). Use loops and conditionals
#  to implement this.


for num in range(1, 51):
    out = ""

    if num % 3 == 0:
        out += "Fizz"
    if num % 5 == 0:
        out += "Buzz"
    if num % 2 == 0:
        out += "Even"

    print(out or num)


# Create a function unique_chars(text) that takes a string and returns the count of unique
# characters (case-sensitive) using a loop. For example, unique_chars("hello") returns
#  4 (h, e, l, o are unique). Avoid using sets; use a list to track characters and string
#  methods like in for checking.

def unique_chars(text):
    seen = []
    for ch in text:
        if ch not in seen:
            seen.append(ch)
    return len(seen)


print(unique_chars("hello"))


# Write a function swap_pairs(lst) that takes a list and swaps every pair of adjacent
# elements. If the list has an odd length, the last element remains in place. For
# example, swap_pairs([1, 2, 3, 4]) returns [2, 1, 4, 3], and swap_pairs([1, 2, 3])
# returns [2, 1, 3]. Use list methods like indexing and loops.

def swap_pairs(lst):
    swapped = []  # create a new list to store the result

    i = 0
    while i < len(lst):
        if i + 1 < len(lst):
            swapped.append(lst[i + 1])
            swapped.append(lst[i])
            i += 2
        else:
            swapped.append(lst[i])
            i += 1

    return swapped


# Write a function invert_dict(d) that inverts a dictionary, making keys into values and
# values into keys. If multiple keys have the same value, group those keys in a list as
#  the new value. For example, invert_dict({"a": 1, "b": 2, "c": 1}) returns
#  {1: ["a", "c"], 2: ["b"]}. Use dictionary methods like items() and loops.

def invert_dict(d):
    inverted = {}

    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]

    return inverted


# Write a function remove_duplicates(lst) that removes duplicates from a list while
# preserving the original order. Do not use sets. For example,
# remove_duplicates([1, 3, 3, 4, 1, 5]) returns [1, 3, 4, 5]. Use list methods like
#  append() and a loop to check for duplicates.
def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result


print(remove_duplicates([1, 3, 3, 4, 1, 5]))


# Write a function longest_word(sentence) that takes a sentence and returns the longest
#  word. If multiple words have the same maximum length, return the first one. Use
# string methods like split() and a loop. For example, longest_word("I love programming")
#  returns "programming".
def longest_word(sentence):
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("I love programming"))
print(longest_word("Python is fun and powerful"))
print(longest_word("same size word size"))

# Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key
# exists in both dictionaries, sum their values. For example,
# merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) returns {"a": 1, "b": 5, "c": 4}.
# Use dictionary methods like keys() or items() and conditionals.


def merge_dicts(dict1, dict2):
    merge = {}
    for k in set(dict1.keys()).union(dict2.keys()):
        value1 = dict1.get(k, 0)
        value2 = dict2.get(k, 0)
        merge[k] = value1 + value2
    return merge


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))

# Write a function number_pattern(n) that prints a pattern of numbers up to n rows,
# where each row contains numbers from 1 to the row number, but only prints odd numbers.
#  For example, number_pattern(4) should print:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# Use nested loops and conditionals to check for odd numbers.


def number_pattern(n):
    for row in range(1, n + 1):
        line = []
        num = 1
        while len(line) < row:
            if num % 2 == 1:
                line.append(str(num))
            num += 1
        print(" ".join(line))


# Write a function reverse_words(sentence) that takes a sentence and reverses the order
#  of characters in each word while keeping the word order intact. For example,
# reverse_words("Hello World") returns "olleH dlroW". Use string methods like split()
#  and join() and a loop to reverse each word.

def reverse_words(sentence):
    reversed_list = []
    for word in sentence.split():
        reversed_list.append(word[::-1])
    return " ".join(reversed_list)


print(reverse_words("Hello World"))


# Write a function filter_range(lst, min_val, max_val) that takes a list of numbers and
# returns a new list containing only the numbers within the range [min_val, max_val]
#  (inclusive). For example, filter_range([1, 5, 3, 8, 2], 2, 5) returns [5, 3, 2].
#  Use list methods like append() and loops with conditionals.

def filter_range(lst, min_val, max_val):
    result = []
    for num in lst:
        if min_val <= num <= max_val:
            result.append(num)
    return result


print(filter_range([1, 5, 3, 8, 2], 2, 5))
