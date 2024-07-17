class Solution:

    def findMinDiff(self,A,N,M):
        A.sort()
        mini = max(A)
        i=0
        
        for i in range(i,N-M+1):
            diff = abs(A[i]-A[i+M-1])
            mini = min(diff,mini)
        return mini