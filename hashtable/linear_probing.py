KEY_INDEX = 0
VALUE_INDEX = 1

class LinearProbingTable:
    def __init__(self, table_size=4):
        self.size = 0
        self.table = []
        for i in range(table_size):
            self.table.append(None)

    def delete(self, key):
        start_index = hash(key) % len(self.table)

        while self.table[start_index] and self.table[start_index][KEY_INDEX] != key:
            start_index = (start_index + 1) % len(self.table)

        self.table[start_index] = None
        #  Shift all following keys with the same hashcode up one
        previous_index = start_index
        start_index = (start_index + 1) % len(self.table)
        

        while self.table[start_index] and \
            hash(key) % len(self.table) == hash(self.table[start_index]) % len(self.table):

            self.table[previous_index] = self.table[start_index]
            self.table[start_index] = None    
            
            previous_index = start_index
            start_index = (start_index + 1) % len(self.table)
    


    def resize(self):
        # Made a new Array twice the size
        new_table = []
        new_table_size = len(self.table) * 2
        for i in range(new_table_size):
            self.table.append(None)

        # We made the new array be self.table
        old_table = self.table
        self.table = new_table

        # re-inserted all the key-value pairs
        for key, value in old_table:
            self.insert(key, value)
    

    def insert(self, key, value):
        """
        Insert `(key, value)` based on the hashed value of `key`.
        """

        # 1.  Find the index to insert the key, value pair
        start_index = hash(key) % len(self.table)
        # # 2.  Check to see if it's empty
        # if self.table[start_index] is None:
        #     # 2.a  If it is, insert and done!
        #     self.table[start_index] = ( key, value )
        # else:                        
        #     # 2.b  If not change index to the next empty slot and repeat
        #     while self.table[start_index] is not None:
        #         start_index = (start_index + 1) % len(self.table)
            
        #     self.table[start_index] = ( key, value )


        while self.table[start_index] is not None:
            start_index = (start_index + 1) % len(self.table)
        
        self.table[start_index] = (key, value)

        # If successful, increment.
        self.size += 1

        if self.size >= 0.75 * len(self.table):
            self.resize()

    def get(self, key, default=None):
        """
        Return the value stored with `key` or `default` if it is not there.
        """
        start_index = hash(key) % len(self.table)
        index = start_index

        if not self.table[index]:
            return default

        # We need to do this once outside of the loop before we get started.
        current_key, value = self.table[index]
        if current_key == key:
            return value
        index += 1 % len(self.table)

        while index != start_index and self.table[index]:
            current_key, value = self.table[index]
            if current_key == key:
                return value
            index = (index + 1) % len(self.table)

        # Return default if we don't find the key.
        return default
