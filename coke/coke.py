

amountdue = 50
print(f"Amount due: {amountdue}")


while amountdue > 0:
    num = int(input("Enter num: "))

    if num in (25,10,5):
        amountdue -= num

    if amountdue > 0:
        print(f"Amount Due: {amountdue}")

print(f"change: {-amountdue}")
