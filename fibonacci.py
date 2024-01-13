n = int(input("Nhap so: "))
assert n >= 0 and int(n) == n , "n phai la so nguyen duong."
def recursive_fibonacci(n):
  if n in [0,1]:
      return n
  else:
      return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
print(recursive_fibonacci(n))
