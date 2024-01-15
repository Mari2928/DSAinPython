class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = []
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """            
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache[key] = value

        if len(self.keys) > self.capacity:
            del self.cache[self.keys.pop(0)]  


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
