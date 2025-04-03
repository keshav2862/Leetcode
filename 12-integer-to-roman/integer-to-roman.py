class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hmap = {
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50: 'L',
        90:'XC',
        100:'C',
        400: 'CD',
        500:'D',
        900:'CM',
        1000:'M'
    }
        t = num - num%1000
        hm = num%1000 - num%100
        tm = num%100 - num%10
        om = num%10
        print(t,hm,tm,om)
        result = ""
        keys = sorted(hmap.keys(), reverse=True)
        for val in keys:
            while t >= val:
                result += hmap[val]
                t -= val
            while hm >= val:
                result += hmap[val]
                hm -= val
            while tm >= val:
                result += hmap[val]
                tm -= val
            while om >= val:
                result += hmap[val]
                om -= val

        return result