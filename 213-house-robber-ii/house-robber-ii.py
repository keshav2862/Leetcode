class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(numbers):
            c= 0
            pc = 0
            for i in numbers:
                temp = c
                c = max(c,pc+i)
                pc = temp
            return c
        
        n = len(nums)
        if n==1:
            return nums[0]
        ans1 = rob1(nums[0:n-1])
        ans2 = rob1(nums[1:n])
        return max(ans1,ans2)
