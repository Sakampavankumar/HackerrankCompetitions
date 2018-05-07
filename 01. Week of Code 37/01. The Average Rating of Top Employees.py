# This is the solution to https://www.hackerrank.com/contests/w37/challenges/the-average-rating-of-top-employees


def averageOfTopEmployees(rating):
    average = roundi(sum(rating) / len(rating) * 100) / 100
    print('%.2f' % average)


def roundi(a):
    if a % 1 >= 0.5:
        a = a // 1 + 1
    else:
        a = a // 1
    return a


n = int(input())
rating = []
for i in range(n):
    rating_item = int(input())
    if rating_item >= 90:
        rating.append(rating_item)
averageOfTopEmployees(rating)
