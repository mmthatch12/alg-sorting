import sys
def rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    def find_outcome(rounds_left, result):
        if rounds_left ==0:
            outcomes.append(result)
            return

        for play in plays:
            find_outcome(rounds_left - 1, result + [play])

    find_outcome(n, [])

    return outcomes

print(rock_paper_scissors(2))

# O(n)
def getLenghtOfList(l):
    list_length = 0
    for i in l:
        list_length += 1
    return list_length 

# 0(1)
def betterGetLengthOfList(l):
    return len(l)

# time complexity of binary search is log(n)

# 2**1 = 2
# log2(2) = 1

# 2**3 = 8
# log2(8) = 3

# 2**10 = 1024
# log2(1024) = 10

# log2(1,000,000) = 20
# log2(1,000,000,000) = 30