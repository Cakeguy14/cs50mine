class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("not an int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if not isinstance(n, int) or n <0:
            raise ValueError("not an int")
        if self._size + n > self._capacity:
            raise ValueError("no more cookie")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("not an int")
        if n > self._size:
            raise ValueError("more than what we have")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    cookies = Jar()
    cookies.deposit(5)
    print(cookies)
    cookies.withdraw(3)
    print(cookies)


if __name__ == "__main__":
    main()

