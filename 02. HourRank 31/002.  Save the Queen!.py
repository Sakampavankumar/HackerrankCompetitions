# Problem: https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen/problem
# Score: 40


def avg(ans, rest):
    return (sum(ans) + rest) / len(ans)


inv, sold = map(int, input().split())
seconds = list(map(int, input().split()))

seconds = sorted(seconds, key=lambda x: -x)

ans = seconds[:inv]
rest = sum(seconds[inv:])

while avg(ans, rest) < max(ans):
    ans.pop(0)

print(avg(ans, rest))
