class HashTable:
    """
    Time complexity:
        Insert: O(1) - sometimes O(n) because of collisions
        Look up: O(1) - sometimes O(n) because of collisions
        Delete: O(1) - sometimes O(n) because of collisions
    """

    def __init__(self, length):
        self.length = length
        self._data = self._populate_new_static_array()

    def __setitem__(self, key, value):
        """hash_table['key'] = 'value'"""
        address = self._hash(key)
        if not self._data[address]:
            self._data[address] = []

        for idx, (k, v) in enumerate(self._data[address]):
            if k == key:
                self._data[address][idx] = (key, value)
                return

        self._data[address].append((key, value))

    def __getitem__(self, key):
        address = self._hash(key)
        if self._data[address]:
            for record in self._data[address]:
                if record[0] == key:
                    return record[1]
        else:
            raise KeyError(f'Provided "{key}" key does not exist.')

    def _hash(self, value):
        return sum(ord(element) for element in value) % len(self._data)

    def _populate_new_static_array(self):
        return [None for _ in range(self.length)]

    def keys(self):
        return [record[0] for bucket in self._data if bucket for record in bucket]

    def values(self):
        return [record[1] for bucket in self._data if bucket for record in bucket]

    def clear(self):
        self._data = self._populate_new_static_array()
