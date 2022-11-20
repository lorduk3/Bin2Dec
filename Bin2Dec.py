def Bin2Dec(binary):
    decimal, i = 0,len(binary)
    for x in binary:
        i -= 1
        decimal += int(x) * pow(2,i)
    return decimal
    
binary = input('Enter a binary number (max 8 characters): ')    

if len(binary) != 8:
    print("Error! Enter a binary number of length 8")
    
for s in binary:
    if s not in {'0','1'}:
        print("Must only contains 0's and 1's !")
        break
    
print("The decimal number is: ", Bin2Dec(binary))
