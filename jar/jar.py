class Jar:
    def __init__(self, capacity=12):
        if not capacity.isdigit():
            raise ValueError("not an int")
        self.capacity = capacity

    def __str__(self):
        return f"{self.capacity} * 🍪"

    def deposit(self, n):
        if n < self.capacity:
            self.capacity += n
            return self.capacity
        else:
            raise ValueError("no more cookie")

    def withdraw(self, n):
        if n < self.capcity:
            self.capacity -= n
            return self.capacity
        else:
            raise ValueError("more than what we have")


    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self, capacity=0):
        return self.capacity


cookies = Jar()
deposit = cookies.deposit(5)
print(cookies.capacity)

