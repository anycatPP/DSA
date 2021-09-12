from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        S = list(S)
        for i in range(len(indexes)):
            k,j = indexes[i],0
            status = True
            while k < len(S) and j < len(sources[i]):
                if S[k] != sources[i][j]:
                    status = False
                k += 1
                j += 1
            if j >= len(sources[i]) and status:
                S[indexes[i]] = targets[i]
                for v in range(indexes[i]+1,indexes[i]+j):
                    S[v] = ""
        return "".join(S)
                    