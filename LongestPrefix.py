class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]
        longest_pre =[]
        for i in range(len(first)):
            if first[i] == last[i]:
              longest_pre.append(first[i])
            else:
                break

        return "".join(longest_pre)