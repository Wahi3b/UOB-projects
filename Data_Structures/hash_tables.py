class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr= [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for ch in key:
            h += ord(ch)
        return h % self.MAX
    

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        
    def __setitem__(self,key,value):
        h= self.get_hash(key)
        found=False
        
        for index,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def delete(self,key,):
        h= self.get_hash(key)
        self.arr[h]= None
    
wahib =HashTable()
wahib['Jan 30th']=30
wahib['Jan 12th']=30
wahib['Jan 12th']=22

print(wahib.arr)
    