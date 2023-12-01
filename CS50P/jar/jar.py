class Jar:
    def __init__(self, capacity = 12, size = 0):
        self.capacity = capacity
        self.size = size


    def __str__(self):
        str = ""
        i = 0
        while i < self.size:
            str += "🍪"
            i += 1
        return str

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies to add")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There aren’t many cookies in the cookie jar to eat")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("The capacity must be a positive value")
        self._capacity = capacity

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size