a='1101'
b='1110'
c='1111'
bina=int(a,2)
binb=int(b,2)
binc=int(c,2)
if bina>binb and bina>binc:
    print("Greatest is", a)
elif binb>bina and binb>binc:
    print("Greatest is", b)
else:
    print("Greatest is", c)
