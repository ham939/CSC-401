class DoubleHashTable:
    def __init__(self, size=16):
        self.table = [None] * size
        self.size = size
    
    def h1(self, key):
        return key % 16
    
    def h2(self, key):
        return 2 * (key % 4) + 1
    
    def insert(self, key):
        index = self.h1(key)
        probe_count = 0
        
        while self.table[index] is not None and probe_count < self.size:
            print(f"Collision at index {index} for key {key}. Probe: {probe_count}")
            probe_count += 1
            index = (self.h1(key) + probe_count * self.h2(key)) % self.size
            
        if probe_count < self.size:
            self.table[index] = key
            print(f"Key {key} inserted at index {index}. Probe: {probe_count}")
            print(self.table)
        else:
            print(f"Table is full! Could not insert key {key}.")
    
    def __str__(self):
        return str(self.table)



# testing
hash_table = DoubleHashTable()

keys_to_insert = [10, 26, 30, 42, 18, 54, 31]

for key in keys_to_insert:
    hash_table.insert(key)
    print("="*30, "\n")
