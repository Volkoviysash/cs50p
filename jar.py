class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity        
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit (self, number):
        if number > self.capacity:
            raise ValueError("Exceed capacity")
        if number + self.size > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += number

    def withdraw(self, number):
        if self._size < number :
            raise ValueError("There are less cookies than asked to remove")            
        else:
            self._size -= number

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(10)
    jar.deposit(10)   
    jar.withdraw(9)    
    print(jar)


if __name__ == "__main__":
    main()