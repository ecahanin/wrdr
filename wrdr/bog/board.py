from .tile import Tile
from .wordlists import build_dicts
import random

checker, valid_words = build_dicts()

LETTERS = {
    'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2, 'G':3, 'H':2, 'I':9, 'J':1,
    'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6,
    'U':4, 'V':2, 'W':2, 'X':1, 'Y':2, 'Z':1
}

class Board():
    def __init__(self, size):
        self.size = size
        self.grid = self.prepare_grid()
        self.config_tiles()
        self.populate_tiles()
        self.checker, self.valid_words = build_dicts()
        
    def __str__(self):
        output = '+' + '---+' * self.size + '\n'
        for row in self.each_row():
            body = '|'
            bottom = '+'
            for tile in row:
                body += " {} |".format(tile.letter)
                bottom += "---+"
            output += body + '\n'
            output += bottom + '\n'
        return output
            
                
    def prepare_grid(self):
        grid = [[] for i in range(self.size)]
        for row in range(self.size):
            grid[row] = [Tile(row, col) for col in range(self.size)]
        return grid
    
    def config_tiles(self):
        for tile in self.each_tile():
            row, col = tile.row, tile.column
            tile.north = self.cell_if_in_grid(row-1,col)
            tile.nw = self.cell_if_in_grid(row-1,col-1)
            tile.ne = self.cell_if_in_grid(row-1,col+1)
            tile.south = self.cell_if_in_grid(row+1,col)
            tile.se = self.cell_if_in_grid(row+1,col+1)
            tile.sw = self.cell_if_in_grid(row+1,col-1)
            tile.west = self.cell_if_in_grid(row,col-1)
            tile.east = self.cell_if_in_grid(row,col+1)
            
    def cell_if_in_grid(self, row, col):
        if 0 <= row < self.size and 0<= col < self.size:
            return self.grid[row][col]
        else:
            return None
    
    def populate_tiles(self):
        for tile in self.each_tile():
            weighted_letters = ''
            for letter, freq in LETTERS.items():
                weighted_letters += letter * freq
            tile.letter = random.choice(weighted_letters)
            
    def each_row(self):
        for row in self.grid:
            yield row
            
    def each_tile(self):
        for row in self.each_row():
            for tile in row:
                yield tile
    
    def tile(self, row, col):
        if (0 <= row <= self.size) and (0 <= col <= self.size):
            return self.grid[row][col]
        else:
            return None
        
    def find_words(self):
        self.words = []
        deadpaths = []

        for tile in self.each_tile():
            path  = [tile]
            while path:
                current = path[-1]
                wordstring = ''
                for tile in path:
                    wordstring += tile.letter
                if wordstring in valid_words and wordstring not in self.words:
                    self.words.append(wordstring)
                unvisited = []
                neighbors = current.neighbors()
                for tile in neighbors:
                    foo = path[:]
                    foo.append(tile)
                    if tile not in path and foo not in deadpaths:
                        unvisited.append(tile)
                if unvisited:
                    next_tile = random.choice(unvisited)
                    wordstring += next_tile.letter
                    path.append(next_tile)
                    if (2 <= len(wordstring) <15 and wordstring in checker[len(wordstring)]) or wordstring in valid_words:
                        pass
                    else:
                        deadpaths.append(path[:])
                        path.pop()     
                else:
                    deadpaths.append(path[:])
                    path.pop()

                
def get_dicts():
    checker, valid_words = build_dicts()
    return checker, valid_words