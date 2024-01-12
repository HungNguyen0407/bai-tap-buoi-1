a = int(input('nhap a:'))
b = int(input('nhap b:'))
if a < 0:
    a == a + a*2
elif b < 0:
    b == b + b*2
def gcd(a,b):
    if b == 0:
        return a 
    else: 
        return gcd(b,a%b)
print('uoc chung lon nhat cua',a,'va',b,'la',gcd(a,b))
