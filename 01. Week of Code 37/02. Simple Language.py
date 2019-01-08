# Problem: https://www.hackerrank.com/contests/w37/challenges/simple-language/problem
# Score: 20


def maximumProgramValue(n):
    maxValue = 0
    for i in range(n):
        string = list(input().split())
        if string[0] == 'set':
            maxValue = max(int(string[1]), maxValue)
        elif string[0] == 'add':
            maxValue += max(int(string[1]), 0)
    return maxValue


n = int(input())
result = maximumProgramValue(n)
print(result)
