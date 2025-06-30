def reverse_string(s):
    result = ""
    for letter in s[::-1]:
        result = result + letter
    return result


print(reverse_string("hello"))


# Create a function is_palindrome that takes a string and returns True if it is a palindrome
#  (reads the same forwards and backwards), False otherwise. Ignore case and non-alphabetic characters.
def is_palindrome(text):
    cleaned = ""
    for letter in text:
        if letter.isalpha():
            cleaned = cleaned + letter.lower()

    if cleaned == reverse_string(cleaned):
        return True
    else:
        return False


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Hello"))


# Use string formatting to create a function greet_user that takes a name and an age and
#  returns a string like "Hello, [name]! You are [age] years old."
def greet_user(name, age):          # name & age are parameters
    return f"Hello, {name}! You are {age} years old."


result = greet_user("Bittisha", 21)
print(result)


# Write a function count_vowels that takes a string and returns the number of vowels
#  (a, e, i, o, u, both lowercase and uppercase) in it.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in s:
        if letter in vowels:
            count = count + 1
    return count


text = "Binita Adhikari"
print(count_vowels(text))


# Create a function rectangle_area that takes two parameters, length and width (with width
# defaulting to 1), and returns the area of the rectangle.
def rectangle_area(length, width=1):
    return length * width


print(rectangle_area(5, 3))
print(rectangle_area(4))


# Write a function print_details that takes three parameters: name, age, and city,
# and prints them in the format "Name: [name], Age: [age], City: [city]". Call this function using keyword arguments.
def print_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


print_details(name="Bob", age=25, city="London")
print_details(age=40, city="Tokyo", name="Anna")


# Define a lambda function that takes a number and returns its square. Assign it to a
# variable called square.
def square(x):
    return x * x


print(square(6))
print(square(10))


# Write a function double_list that takes a list of numbers and returns a new list
#  where each element is doubled. Use a loop instead of map().
def double_list(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


print(double_list([1, 3, 5]))  # Output: [2, 6, 10]


# Write a function get_evens that takes a list of numbers and returns a new list containing
# only the even numbers. Use a loop instead of filter().
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


print(get_evens([10, 15, 22, 33, 40]))  # Output: [10, 22, 40]


# Write a function sort_by_age that takes a list of tuples (name, age) and returns a new list
#  sorted by age in ascending order. Use a simple sorting algorithm (e.g., bubble sort) instead of sorted().


# Write a function capitalize_words that takes a sentence (a string) and returns a new sentence
# where the first letter of each word is capitalized.
def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


sentence = "hello! my name is binita."
print(capitalize_words(sentence))


# Create a function replace_substring that takes three strings: the original string, the
#  substring to replace, and the replacement string. Return the modified string with all
# occurrences of the substring replaced.
def replace_substring(original, to_replace, replacement):
    return original.replace(to_replace, replacement)


original = "I like apples. Apples are tasty."
to_replace = "apples"
replacement = "oranges"
print(replace_substring(original, to_replace, replacement))


# Write a function reverse_all that takes a list of strings and returns a new list where each string is reversed.
def reverse_all(strings):
    return [s[::-1] for s in strings]


words_list = ["sara", "tara", "para"]
print(reverse_all(words_list))


# Create a function sum_all that accepts any number of numeric arguments and returns their
#  sum. Use *args for variable arguments.
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))


# Write a function calculate_total that takes any number of item prices and an optional
# discount percentage (default to 0). Return the total cost after applying the discount.
def calculate_total(*prices, discount=0):
    total = sum(prices)
    discounted_total = total - (total * discount / 100)
    return discounted_total


print(calculate_total(100, 200, 300, discount=10))
