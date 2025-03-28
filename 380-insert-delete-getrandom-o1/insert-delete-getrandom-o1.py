class RandomizedSet(object):

    def __init__(self):
        self.rmap = {}
        self.rlist =[]
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.rmap:
            self.rmap[val] = len(self.rlist)
            self.rlist.append(val)            
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rmap:
            idx = self.rmap[val]
            lastval = self.rlist[-1]
            self.rlist[idx] = lastval
            self.rlist.pop()
            self.rmap[lastval] = idx
            del self.rmap[val]
            return True
        return False
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.rlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()