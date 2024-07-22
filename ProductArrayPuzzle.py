class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        prefix = [1]*n
        surfix = [1]*n
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(n-2, -1,-1):
            surfix[i] = surfix[i+1] * nums[i+1]
        res = [prefix[i]*surfix[i] for i in range(n)]
        return res