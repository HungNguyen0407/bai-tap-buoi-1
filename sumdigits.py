i = int(input('Nhap 1 so: '))
def sumdigits(i):
    if i in [0,9]:
        return i
    return i % 10 + sumdigits(int(i/10))
print('Ket qua la: ', sumdigits(i))