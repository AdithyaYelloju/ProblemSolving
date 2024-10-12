class LRU:


    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity


    def put(self, key, value):
        if(self.cache.get(key, False)):
            del self.cache[key]


        self.cache[key] = value


        if(len(self.cache) > self.capacity):
            del self.cache[list(self.cache.keys() )[0]]


   


    def get(self, key):
        value = self.cache.get(key, -1)
        if value == -1:
            return value


        del self.cache[key]
        self.cache[key] = value
        return value


    def print_cache(self):
        print(self.cache)




cache = LRU(3)
cache.put(key=1, value='A')
cache.put (key=2, value='B')
cache.print_cache()


cache.put (key=3, value='C')
cache.print_cache()


print(cache.get(key=2))
cache.print_cache()


print(cache.get(key=4))


cache.put (key=4, value='D')
cache.print_cache()


cache.put (key=3, value='E')
cache.print_cache()


cache.get(key=4)
cache.print_cache()


cache.put(key=1, value='A')
cache.print_cache()
