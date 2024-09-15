class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError()
        self.cookies = 0
        self._capacity = capacity

    def __str__(self):
        string = ""
        for _ in range(self.cookies):
            string += "🍪"
        return  f"{string}"
    
    def deposit(self, n):
        if  type(n) == int and self.cookies + n <= self._capacity:
            self.cookies += n
        else:
            raise ValueError()
    
    def withdraw(self, n):
        if isinstance(n, int) and self.cookies - n >= 0:
            self.cookies -= n
        else:
            raise ValueError()
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self.cookies