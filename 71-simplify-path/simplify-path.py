class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        dirs = path.split("/")
        for x in dirs:
            if x == '.' or not x:
                continue
            elif x =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return "/" + "/".join(stack)