i = int(input('Nhap 1 so: '))
assert i > 9 and int(i) == i ,'so nguyen duong >= 10'
def sumdigits(i):
    if i in [0,9]:
        return i
    return i % 10 + sumdigits(int(i/10))
print('Ket qua la: ', sumdigits(i))