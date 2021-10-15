class LinearProbingTable:
    def __init__(self, table_size=4):
        self.size = 0
        self.table = []
        for i in range(table_size):
            self.table.append(None)

    def insert(self, key, value):
        """
        Insert `(key, value)` based on the hashed value of `key`.
        """

        # TODO: Try to insert into self.table

        # If successful, increment.
        self.size += 1

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
