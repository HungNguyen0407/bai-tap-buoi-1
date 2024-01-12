n = int(input('Nhap so bat ki:'))
assert n>=0 , 'Vui long nhap so nguyen duong'
def DtoB(n):
    if n==0:
        return n
    else:
        return n % 2 + 10 * DtoB(n//2)
print('Ket qua la:', DtoB(n))

    