import random

from hashtable.linear_probing import LinearProbingTable

def test_insert():
    nums = []
    # Get a unique random number.
    #
    # This is mostly me being paranoid about bad luck.
    def get_unique_num():
        num = random.randint(-10000, 10000)
        while num in nums:
            num = random.randint(-10000, 10000)
        nums.append(num)
        return num

    table = LinearProbingTable()

    for size in range(1, 5):
        key = get_unique_num()
        val = get_unique_num()

        table.insert(key, val)

        assert table.size == size
        assert table.get(key) == val

    # Check for missing keys.
    assert table.get(get_unique_num()) == None
    assert table.get(get_unique_num(), "missing") == "missing"

def test_delete():
    nums = []

    # Get a unique random number.
    #
    # This is mostly me being paranoid about bad luck.
    def get_unique_num():
        num = random.randint(-10000, 10000)
        while num in nums:
            num = random.randint(-10000, 10000)
        nums.append(num)
        return num

    table = LinearProbingTable()

    keys_in_table = []

    for size in range(1, 5):
        key = get_unique_num()
        val = get_unique_num()

        table.insert(key, val)
        keys_in_table.append(key)

    
    for num in keys_in_table:
        assert table.get(num)
        table.delete(num)
        assert table.get(num) is None      
    
def test_insert_more_than_10():
    nums = []

    # Get a unique random number.
    #
    # This is mostly me being paranoid about bad luck.
    def get_unique_num():
        num = random.randint(-10000, 10000)
        while num in nums:
            num = random.randint(-10000, 10000)
        nums.append(num)
        return num

    table = LinearProbingTable()

    keys_in_table = []

    for size in range(1, 12):
        key = get_unique_num()
        val = get_unique_num()

        table.insert(key, val)
