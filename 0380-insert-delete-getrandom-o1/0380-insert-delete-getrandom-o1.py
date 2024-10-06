class RandomizedSet(object):

    def __init__(self):
        self.index={}
        self.value=[]

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.value:
            return False
        self.index[val]=len(self.value)
        self.value.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        index_rem=self.index[val]
        last_ele=self.value[-1]
        self.value[index_rem] = last_ele
        self.index[last_ele] = index_rem
        self.value.pop()
        del self.index[val]
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.value)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()