class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row[:] = row[::-1]
            
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0

                else:
                    row[i]=1

        return image