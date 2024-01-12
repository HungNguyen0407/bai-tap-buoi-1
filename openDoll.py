x = int(input('insert number of dolls: '))
assert x > 0 and int(x) == x , 'the number of dolls must be a positive integer'
def openDoll(i):
    if i == 1:
        print('All dolls are opened')
        return
    print('Open doll',i)
    n = i - 1
    openDoll(n)
openDoll(x)