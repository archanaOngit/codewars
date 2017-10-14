# Your task is to make a program takes in a sentence (without punctuation), adds all words to a list and returns the
# sentence as a string which is the positions of the word in the list. Casing should not matter too.
#
# Example
#
# "Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"
#
# becomes
#
# "01234567802856734"
#
# Another example
#
# "the one bumble bee one bumble the bee"
#
# becomes
#
# "01231203"


def compress_sentence(sentence):
    arr = sentence.lower().split(" ")
    output = ''
    unique_arr = []
    for word in arr:
        if word not in unique_arr:
            unique_arr.append(word)
    for word in arr:
        for i in range(len(unique_arr)):
            if word == unique_arr[i]:
                output += str(i)
    return output


# Remove all duplicates from a given string
# Sample string : geeksforgeeks
# Output : geksfor


def remove_dups(string):
    output = ''
    #temp = ''.join(sorted(string)) This is just if we want to maintain the order of characters as well.
    for each in string:
        if each not in output:
            output += str(each)
    print output
    return output


# A Python Program to check if the given string is a pangram or not
# Check your code against :- "The quick brown fox jumps over the little lazy dog"

def check_panagram(string):
    List = []
    for i in range(26):
        List.append(False)

    for c in string.lower():
        if not c == " ":
            List[ord(c) - ord('a')] = True

    for ch in List:
        if ch is False:
            return False
    return True

# Function to remove all spaces from a given string


def remove_spaces(string):
    output = []
    for i in range(len(string)):
        if string[i] != ' ':
            output.append(string[i])
    return ''.join(output)


# Return maximum occurring character in an input string

def max_occurrence(string):
    List = {}
    for each in string.lower():
        if each not in List.keys():
            List.update({each: 1})
        else:
            val = List[each]
            List[each] = val + 1
    sortedItems =  sorted(List, key=List.get, reverse=True)
    for element in sortedItems:
        print (element, List.get(element))


# You are given some denominations of coins in an array (int denom[])and infinite supply
# of all of them.Given an amount (int amount), find the minimum number of coins required to get the exact amount.
# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required
# We can use one coin of 25 cents and one of 5 cents

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required
# We can use one coin of 6 cents and 1 coin of 5 cents


# import sys


def minimum_coins(coins, amount):
    import sys
    denominations = [1, 3, 5]
    coins_needed = [sys.maxint] * 20
    coins_needed[0] = 0

    for amt in range(20):
        for coin in denominations:
            if coin <= amt and coins_needed[amt - coin] + 1 < coins_needed[amt]:
                coins_needed[amt] = coins_needed[amt - coin] + 1

    print coins_needed



def find_change(coins, money):
    denominations = [5, 10, 25]
    coins_needed = [0]

    for amt in range(1, 30):
        coins_needed.append(min(
            1 + coins_needed[amt - coin] for coin in denominations if coin <= amt
        ))

    print(coins_needed)


# Function to print Longest common subsequence
def find_substring(a_string, substring):
    for i in range(len(a_string)):
        if a_string[i] == substring[0] and a_string[i:i+len(substring)] == substring:
            print(i)
            return
    else:
        print(False)
        # def longest_common_subsequence(seq, subseq):
        # return





