class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0 , len(nums)-1
        i = 0
        def swap(i,j):
            temp = nums[i]
            nums[i]= nums[j]
            nums[j]=temp

        while i <=r:
            if nums[i]== 0:
                swap(i,l)
                l+=1

            elif nums[i]==2:
                swap(r,i)
                r-=1
                i-=1
            i+=1

        