# Problem: https://www.hackerrank.com/contests/hourrank-31/challenges/hanging-posters/problem
# Score: 15


import math
n, h = map(int, input().split())
wallPoints = list(map(int, input().rstrip().split()))
lengths = list(map(int, input().rstrip().split()))
ans_arr = [wallPoints[i] - lengths[i]*0.25 for i in range(len(wallPoints))]
print(max(math.ceil(max(ans_arr)) - h, 0))
