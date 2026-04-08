#https://cs50.harvard.edu/python/psets/8/jar/


class Jar:
    def __init__(self,capacity=12):
        self.capacity = capacity
        self.size = 0
    def __str__(self):
        return f"{"🍪" * self.size}"

    #deposit a cookie coo
    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Sumosobra ka na par!")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Asa man na nimo kuhaon nga cookie daw bi?")
        self.size -= n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError
        self._capacity = value

    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, value):
        if value > self.capacity:
            raise ValueError
        self._size = value