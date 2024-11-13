data = [(name,phone) for name,phone in [i.split(',') for i in input().split()]]
theName = input()

for i in data:
    if i[0] == theName:
        print(i[1])
        break
