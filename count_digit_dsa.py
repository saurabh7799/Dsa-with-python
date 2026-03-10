# def count_digits(n):
#     count=0
#     while n>0:
#         count+=1
#         n=n//10
#     return count
# print(count_digits(12345))

from numpy import log10


def count_digits(n):
    return int(log10(n)) + 1
print(count_digits(12345))