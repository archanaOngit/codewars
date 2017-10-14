# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

def invert(array):
    for i in range(len(array)):
        array[i] = -array[i]
    print (array)


# Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.
# For start = 125, and end = 132, The digit frequencies are 1 x 0, 9 x 1, 6 x 2 etc...
# and so the method would return [1,9,6,3,0,1,1,1,1,1]


def tribonacci(signature, n):
    output = []
    l = len(output)
    if n == 0:
        return output
    output = output + signature
    if n <=len(output):
        return output[0:n]
    while n > len(output):
        output.append(output[l-1] + output[l-2] + output[l-3])
    return output


# Create a function named divisors/Divisors that takes an integer and returns an array with all of the integer's
# divisors (except for 1 and the number itself). If the number is prime return the string '(integer) is prime'
# (null in C#)(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
#
# Example:
#
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"
# You can assume that you will only get positive integers as inputs.

def divisors(integer):
    Divisors = []
    for n in range(2, integer):
        if integer % n == 0:
            Divisors.append(n)
    return Divisors


# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata

def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    return count











