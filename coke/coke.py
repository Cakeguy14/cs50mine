

amountdue = 50
print(amountdue)


while amountdue > 0:
    num = int(input("Enter num: "))
    if num in (25,10,5):
        amountdue -= num
    if amountdue > 0:
            print(f"amount due: {amountdue}")
    else:
        print(amountdue)
