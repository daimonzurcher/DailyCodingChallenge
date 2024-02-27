''' Problem Statement: Create a dynamic array structure from scratch that can automatically
resize itself as elements are added or removed. Your implementation should support basic
operations such as add, remove, and access by index.

Example Operations:

Add an element to the array.

Remove an element from a specific index.

Access an element at a given index.

Guidelines:

Choose any programming language to implement your dynamic array.

Focus on the efficiency of resizing operations.

Bonus Challenge: Implement additional features like iterator support or sorting within the dynamic array. '''

# create class for array
class DynamicArray:
    def __init__(self):
        self.capacity = 1  # initial capacity
        self.size = 0  # current size
        self.array = [None] * self.capacity  # initialize array - all with None values

    # resize function
    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # add function
    def add(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)  # double capacity if array is full
        self.array[self.size] = element
        self.size += 1

    # remove function (from specific index)
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        # Shrink the array if size is less than or equal to 1/4 of capacity
        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

    # access function (at given index)
    def access_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __str__(self):
        return str(self.array[:self.size])


# example of use
arr = DynamicArray()

# add elemenents to the array
arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
arr.add(5)

# output initial array
print("Initial Array =", arr)

# output array after removing an index
arr.remove_at(2)  # remove element at index 2
print("After removal of index 2 =", arr)

# output specific element being accessed
print("Element at index 1 =", arr.access_at(1))