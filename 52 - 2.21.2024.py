''' Problem Statement: Create an efficient data structure to manage a collection of data points
(e.g., student records, inventory items, etc.) that supports fast retrieval, insertion, and
deletion. Your data structure should optimize for performance based on specific access patterns described below.

Access Patterns:

Retrieve items by a unique identifier.

Insert new items while maintaining sorted order by a specified attribute.

Delete items based on a condition.

Guidelines:

Implement your solution in any programming language.

Consider the trade-offs of different data structures (e.g., arrays, linked lists, trees, hash maps) for the tasks at hand.

Bonus Challenge: Implement custom functionality that showcases the unique strengths of your chosen data structure.'''

# data structure using both a hash map and BST (sorted data)
class DataStructure:
    def __init__(self):
        self.hash_map = {}  # use this for fast retrieval by unique identifier
        self.sorted_data = []  # use for maintaining sorted order by a specified attribute
    
    def retrieve_by_id(self, unique_id):
        return self.hash_map.get(unique_id, None)
    
    def insert_sorted(self, item, key):
        # find correct position to insert item based on specified attribute
        index = len(self.sorted_data)
        for i, (existing_id, _) in enumerate(self.sorted_data):
            if getattr(item, key) < getattr(self.hash_map[existing_id], key):
                index = i
                break
        self.sorted_data.insert(index, (item.id, item))
        self.hash_map[item.id] = item
    
    def delete_by_condition(self, condition):
        # delete items based on a given condition
        self.sorted_data = [item for item in self.sorted_data if not condition(item[1])]
        self.hash_map = {item[0]: item[1] for item in self.sorted_data}

# demonstrating usage --> Student class representing student records
class Student:
    def __init__(self, student_id, name, score):
        self.id = student_id
        self.name = name
        self.score = score

# instance of the DataStructure class
data_structure = DataStructure()

# insert mock student records while maintaining sorted order (by score)
data_structure.insert_sorted(Student(1001, "Charlie", 85), "score")
data_structure.insert_sorted(Student(1002, "Dennis", 92), "score")
data_structure.insert_sorted(Student(1003, "Frank", 78), "score")

# delete student records based on a condition --> example I'm using is: delete students who scored less than 85
data_structure.delete_by_condition(lambda student: student.score < 84)

# print remaining student records
for data in data_structure.sorted_data:
    item_id, item = data
    if item is not None:
        print(item_id, item.name, item.score)