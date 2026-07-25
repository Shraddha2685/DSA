class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(s)
        seen = set()
        result = []

        for i in s:
            if i.isnumeric():
                if i not in seen:
                    seen.add(i)
                    result.append(int(i))

        result.sort()
        if len(result)<2:
            return -1

        return result[-2]