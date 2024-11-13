numbers = [int(i) for i in input().split() if int(i)<0]
numbers.sort()
numbers.reverse()
print(' '.join([str(i) for i in numbers]), end=' ')
