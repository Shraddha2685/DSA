class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string:str) -> list[str]:
            stack = []

            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return stack
        
        return build_string(s) == build_string(t)