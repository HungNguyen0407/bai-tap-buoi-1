n = int(input("Nhap so: "))
assert n >= 0 and int(n) == n , "n phai la so nguyen duong."
def giaithua(n):
    if n in [0,1]: 
        return 1
    else:
        return n * giaithua(n-1)
print('Giai thua cua',n,'=', giaithua(n))
