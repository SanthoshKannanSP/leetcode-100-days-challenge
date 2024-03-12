class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = ord(coordinates[0]) - 97
        col = int(coordinates[1]) - 1

        return (row+col)&1==1