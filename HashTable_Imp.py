class HashTable:
    def __init__(self,size):
        self.size=size
        self.table = [[] for _ in range(size)]

    def hash_func(self,key):
        hash=0
        for i in range(0,len(key)):
            hash=(hash+ord(key[i])*i)%len(key)
        return hash

    def insert(self,key,value):
        index=self.hash_func(key)
        self.table[index].append((key,value))

    def delete(self,key):
        index=self.hash_func(key)
        for i,(k,_) in enumerate(self.table[index]):
            if k==key:
                del self.table[index][i]
                return

    def get(self,key):
        index=self.hash_func(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                return v
            
hash_table =HashTable(20)
hash_table.insert("apple",20)
print(hash_table.get("apple"))
hash_table.delete("apple")
print(hash_table.get("apple"))

