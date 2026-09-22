

amountdue = 50
print(f"Amountdue: {amountdue}")


while amountdue > 0:
    num = int(input("Enter num: "))

    if num in (50,25,10,5):
        amountdue -= num
    if amountdue > 0:
            print(f"amount due: {amountdue}")
    else:
        print(f"Amountdue: {amountdue}")
