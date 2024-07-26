class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        l = 0
        r = N -k
        total= 0

        for i in range(r,N):
            total += cardPoints[i]
        res = total
        while r < N:
           total += cardPoints[l] - cardPoints[r]
           res = max(res, total)
           l+=1
           r+=1

        return res
                