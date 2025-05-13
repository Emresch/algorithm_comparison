import time
import random

# Part 1: Sorting Algorithms

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left = arr[:mid]     
        right = arr[mid:]    

        merge_sort(left)     
        merge_sort(right)   
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left, if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right, if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]                            # Choose pivot element
    left = [x for x in arr if x < pivot]                  # Elements less than pivot
    middle = [x for x in arr if x == pivot]               # Elements equal to pivot
    right = [x for x in arr if x > pivot]                 # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)

# Measure execution time for sorting algorithms
def measure_sorting_time():
    # Define input instances
    instance1 = [random.randint(1, 100000) for _ in range(100000)]    # Random input (Instance 1)
    instance2 = [i for i in range(100000)]                            # Sorted input (Instance 2)

    # Measure Merge Sort on instance1
    start = time.time()
    merge_sort(instance1.copy())
    merge_time_instance1 = time.time() - start

    # Measure Quick Sort on instance1
    start = time.time()
    quick_sort(instance1.copy())
    quick_time_instance1 = time.time() - start

    # Measure Merge Sort on instance2
    start = time.time()
    merge_sort(instance2.copy())
    merge_time_instance2 = time.time() - start

    # Measure Quick Sort on instance2
    start = time.time()
    quick_sort(instance2.copy())
    quick_time_instance2 = time.time() - start

    print("Instance 1: Random Input")
    print(f"Merge Sort Time: {merge_time_instance1:.6f}s")
    print(f"Quick Sort Time: {quick_time_instance1:.6f}s")

    print("\nInstance 2: Nearly Sorted Input")
    print(f"Merge Sort Time: {merge_time_instance2:.6f}s")
    print(f"Quick Sort Time: {quick_time_instance2:.6f}s")

# Part 2: Search Algorithms

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def get(self, key):
        index = self._hash(key)
        return key in self.table[index]

# Measure execution time for search algorithms
def measure_searching_time():

    sequence1 = [("put", 5), ("put", 10), ("put", 3), ("get", 10), ("get", 5), ("get", 7)]
    sequence2 = [("put", 2), ("put", 4), ("put", 1), ("get", 3), ("get", 4), ("put", 6), ("get", 6)]

    # Test Binary Search Tree on sequence 1
    bst = BinarySearchTree()
    start = time.time()
    for operation in sequence1:
        if operation[0] == "put":
            bst.insert(operation[1])
        elif operation[0] == "get":
            bst.search(operation[1])
    bst_time_sequence1 = time.time() - start

    # Test Hash on sequence 1
    hash_table = HashTable(10)
    start = time.time()
    for operation in sequence1:
        if operation[0] == "put":
            hash_table.put(operation[1])
        elif operation[0] == "get":
            hash_table.get(operation[1])
    hash_table_time_sequence1 = time.time() - start

    print("Sequence 1:")
    print(f"Binary Search Tree Time: {bst_time_sequence1:.6f}s")
    print(f"Hash Table Time: {hash_table_time_sequence1:.6f}s")

     # Test Binary Search Tree on sequence 2
    bst = BinarySearchTree()
    start = time.time()
    for operation in sequence2:
        if operation[0] == "put":
            bst.insert(operation[1])
        elif operation[0] == "get":
            bst.search(operation[1])
    bst_time_sequence2 = time.time() - start

    # Test Hash Table on sequence 2
    hash_table = HashTable(10)
    start = time.time()
    for operation in sequence2:
        if operation[0] == "put":
            hash_table.put(operation[1])
        elif operation[0] == "get":
            hash_table.get(operation[1])
    hash_table_time_sequence2 = time.time() - start

    print("\nSequence 2:")
    print(f"Binary Search Tree Time: {bst_time_sequence2:.6f}s")
    print(f"Hash Table Time: {hash_table_time_sequence2:.6f}s")


# Run the experiments
if __name__ == "__main__":
    print("Sorting Algorithm Comparison:\n")
    measure_sorting_time()
    print("\nSearching Algorithm Comparison:\n")
    measure_searching_time()
