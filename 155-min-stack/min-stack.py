class MinStack(object):

    def __init__(self):
        self.st=[]
        self.minst = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.st.append(val)
        if not self.minst or val<= self.minst[-1]:
            self.minst.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        if self.st.pop() == self.minst[-1]:
            self.minst.pop()

    def top(self):
        """
        :rtype: int
        """
        return -1 if not self.st else self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return -1 if not self.minst else self.minst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()