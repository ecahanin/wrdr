class Tile():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.letter = ''

        
    def neighbors(self):
        neighbors = []
        if self.north:
            neighbors.append(self.north)
        if self.south:
            neighbors.append(self.south)
        if self.east:
            neighbors.append(self.east)
        if self.west:
            neighbors.append(self.west)
        if self.ne:
            neighbors.append(self.ne)
        if self.nw:
            neighbors.append(self.nw)
        if self.se:
            neighbors.append(self.se)
        if self.sw:
            neighbors.append(self.sw)
        return neighbors
    
