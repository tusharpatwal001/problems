import ctypes


class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __make_array(self, capacity):
        # creates a C type array(static, referential) with size capacity
        return (capacity*ctypes.py_object)()

    def __resize(self, new_capacity):
        # create a new arry with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]

        # reassign A
        self.A = B

    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)

        # append
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return "Empty list"

        print(self.A[self.n-1])
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError - Item not in list"

    def insert(self, index, item):
        if self.n == self.n:
            self.__resize(self.size*2)

        for idx in range(self.n, index, -1):
            self.A[idx] = self.A[idx-1]

        self.A[index] = item
        self.n += 1

    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ", "

        return "[" + result[:-2] + "]"

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        return "IndexError - Index out of range"


l = MyList()

l.append("hello")
l.append(3.4)
l.append(True)
l.append(100)

print(l)

l.insert(0, 0)
print(l)
