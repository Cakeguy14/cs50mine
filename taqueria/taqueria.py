Item = [{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}]

def main():
    Amount = []
    value = input("Item: ").title()
    while True:
        if value not in Item:
            break
        else:
            Amount += value[key]
        print(f"${Amount:.2f}")
        pass

main()


