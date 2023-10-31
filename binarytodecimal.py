num=input("Enter the binary number:")
bin_num="01"
for i in range(len(num)):
    binary=True
if num[i] not in bin_num:
    print("Invalid input")
    binary=False
if binary:
    dec_number=int(num,2)
    oct_number=oct(dec_number)
    hexa=hex(dec_number)
    print("Decimal Equivalent=",dec_number)
    print("Octal Equivalent=",oct_number)
    print("Hexa Equivalent=",hexa)
