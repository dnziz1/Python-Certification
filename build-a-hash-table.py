class HashTable():
    def __init__(self):
        self.collection = {}

    def hash(self, value: str):
        result = 0
        for char in value:
            result += ord(char)
        return result

    def add(self, key, value):
        hash_value = self.hash(key)

        if hash_value not in self.collection:
            self.collection[hash_value] = {}

        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)
        
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

                if not self.collection[hash_value]:
                    del self.collection[hash_value]
    
    def lookup(self, key):
        hash_value = self.hash(key)

        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
        return None
