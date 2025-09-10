p=1000
s=0
for i in range(1,p):
    if i%3==0 or i%5==0:
        s += i
    elif i%3==0 and i%5==0:
        s += i
    else:
        continue
print(s)

a=0
b=1
k=0
while b <= 4000000:
    c=a+b
    a,b=b,c
    if b%2==0:
        k += b
print(k)