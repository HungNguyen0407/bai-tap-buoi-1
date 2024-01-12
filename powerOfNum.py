x = int(input('Nhap x: '))
y = int(input('nhap y: '))
assert y >= 0, 'so mu nguyen duong'
if x==0 and y==0:
    print('khong xac dinh')
def power(x,y):
    if x==0:
        return 0 
    elif y==0:
        return 1
    else:
        return x*power(x,y-1)
print('Ket qua la: ', power(x,y))