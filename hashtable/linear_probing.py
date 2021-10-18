class LinearProbingTable:
    def __init__(self, table_size=4):
        self.size = 0
        self.table = []
        for i in range(table_size):
            self.table.append(None)

    def resize(self):
        #make new array twice the size
        new_table = []
        new_table_size = len(self.table)*2
        for i in range(new_table_size):
            self.table.append(None)

        #make new array table
        old_table = self.table
        self.table = new_table

        #re-insert key, value pairs
        for key, value in old_table:
            self.insert(key, value)

    def insert(self, key, value):
        """
        Insert `(key, value)` based on the hashed value of `key`.
        """

        # TODO: Try to insert into self.table

        # find index to insert key-value pair
        start_index = hash(key) % len(self.table)

        # # check to see if empty
        # if self.table[start_index] is None:
        #     # insert index with (key, value) as value
        #     self.table[start_index] = (key, value)
        # # if not empty, change index to next empty spot and repeat
        # else:
        #     while self.table[start_index] is not None:
        #         start_index = (start_index+1) % len(self.table)

        #     self.table[start_index] = (key, value)


        while self.table[start_index] is not None:
            start_index = (start_index+1) % len(self.table)
        
        self.table[start_index] = (key, value)

        # If successful, increment.
        self.size += 1

        if self.size >= 0.75*len(self.table):
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
        index = (index + 1) % len(self.table)

        while index != start_index and self.table[index]:
            current_key, value = self.table[index]
            if current_key == key:
                return value
            index = (index + 1) % len(self.table)

        # Return default if we don't find the key.
        return default
