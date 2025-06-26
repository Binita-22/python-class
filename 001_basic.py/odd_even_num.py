nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_and_even_dic = {}
for num in nums:
    if num % 2 == 0:
        odd_and_even_dic[num] = 'Even'
    else:
        odd_and_even_dic[num] = 'odd'
print(odd_and_even_dic)
