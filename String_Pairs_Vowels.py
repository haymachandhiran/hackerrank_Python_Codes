# One person hands over the list of digits to Mr. String, But Mr. String understands only strings. Within strings also he understands only vowels. Mr. String needs your help to find the total number of pairs which add up to a certain digit D.
#
# The rules to calculate digit D are as follows:
#
# Take all digits and convert them into their textual representation.
# Next, sum up the number of vowels i.e. {a, e, i, o, u} from all textual representation. This sum is digit D.
# Now, once digit D is known find out all unordered pairs of numbers in input whose sum is equal to D.
# Problem Statement: Given an array arr[] consisting of N ( 1 ≤ N ≤ 100 ) integers, the task is to convert each array element ( 1 ≤ arr[i] ≤ 100 ) into their respective textual representations and print the lowercase representation of the count of all possible pairs from the array whose sum is equal to the total count of vowels present in their textual representation. If the count exceeds 100 print “greater 100”.
# Note: For the number 100, convert it to textual representation as hundred and not as one hundred.
#
# Examples:
#
# Input: arr[] = {1, 2, 3, 4, 5}
# Output: one
# Explanation:
# 1 -> one -> o, e (2 vowels)
# 2 -> two -> o (1 vowel)
# 3 -> three -> e, e (2 vowels)
# 4 -> four -> o, u (2 vowels)
# 5 -> five – > i, e (2 vowels)
# The total count of vowels in their textual representations = {2 + 1 + 2 + 2 + 2} = 9.
# Now from the given array, only a single unordered pair {4, 5} sums up to 9. Therefore, the count is 1. Hence, the required output is “one“.
#
#
#
# Input: arr[] = {7, 4, 2, }
# Output: zero
# Explanation:
# 7 -> seven -> e, e (2 vowels)
# 4 -> four -> o, u (2 vowels)
# 2 -> two -> o (1 vowel)
# The total count of vowels in their textual representation = {2 + 2 + 1} = 5.
# Now from the given array, no pair exists which adds up to 5. Therefore, the answer is “zero“.

from num2words import num2words
from itertools import combinations_with_replacement

def find_digits(arr):
    n = len(arr)
    vowels = ['a', 'e', 'i', 'o', 'u']
    dig_count = 0
    words = []
    for i in range(n):
        temp = num2words(arr[i])
        temp = temp.replace('-', '')
        words.append(temp)
    print (words)
    for i in range(n):
        for j in range(len(vowels)):
            if vowels[j] in words[i]:
                # print(words[i].count(vowels[j]))
                dig_count += words[i].count(vowels[j])
    return dig_count
def find_pair(arr, D):
    pairs = list(combinations_with_replacement(arr, 2))
    pair_count = 0
    for j in pairs:
        if sum(j) == D:
            pair_count += 1
    return pair_count

arr = [5, 7, 12, 55, 4]
D = find_digits(arr)
print(D)
res = find_pair(arr, D)
fin_res = num2words(res)
x = fin_res.replace('-', '')
x= x.capitalize()
print(x)