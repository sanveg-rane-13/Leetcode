from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_map = dict()
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data_map:
            return False
        
        self.data.append(val)
        self.data_map[val] = len(self.data) - 1 # save index of new element
        
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.data_map:
            return False
        
        idx = self.data_map[val]
        lstValIdx = len(self.data) - 1
        lstVal = self.data[lstValIdx]
        
        if idx != lstValIdx:
            # swap the target with last element
            self.data[idx], self.data[lstValIdx] = lstVal, val
            self.data_map[lstVal], self.data_map[val] = idx, lstValIdx
            
        del self.data_map[self.data[lstValIdx]]
        del self.data[lstValIdx]
        
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()