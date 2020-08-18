class HashTable:
    def __init__(self):
        # Nb the size is 11 a prime number so that handling of collisions can be as effective as possible.
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, (len(self.slots)))

        # check if the given slot is empty(None) If its is place the key there
        if self.slots[hash_value] == None:
            # place the key into the slots list
            self.slots[hash_value] = key
            # place the data into the data list
            self.data[hash_value] = data
        else:
            # Replace the data if you find that the key already exists
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            # look for the next slot to place the key if collision occurs
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(hash_value, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                # Replace the data if you find that the key already exists
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        # Nb you perform a modulo arithmatic so as to take the index back to 0 if the index is more than the size of the list
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, (len(self.slots)))
        data = None
        stop = False
        found = False
        position = start_slot

        if self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        return self.put(key, item)


if __name__ == "__main__":
    h = HashTable()
    h.put(14, "cat")
    h.put(60, "donkey")
    h.put(77, "elephant")
    h.put(24, "sam")
    h.put(33, "phillix")
    h.put(70, "tommy")

    print(h.data)
