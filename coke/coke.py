
def main():
    amountdue = 50
    num = int(input("Enter num: "))

    while amountdue > 0:
        if num in (25,10,5):
            amountdue -= num
            print(amountdue)
            return amountdue
        else:
            break

main()
