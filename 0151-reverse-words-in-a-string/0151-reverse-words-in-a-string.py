class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        for word in range(len(words)-1,-1,-1):
            result += words[word] + " "
    
        return result.strip()

            

            
