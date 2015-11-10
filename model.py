


# we want to animate the bucket-tool from mspaint-like programs
# we need to come up with a grid of nodes, probably three colors
# colors are ignore, target, and colored


# initialize our grid with colors mapped out
# add a boundary node
# Repeat until no boundary nodes
#   for each boundary node
#       if adjacent target node, add to list (if not already)
#       color boundary node
#   update boundary list with new boundary

class BucketToolField:

    def __init__(self):
        self.width, self.height = 0,0
        self.grid = None
        self.boundary = set()
        self.visited = set()
        self.updates = set()

    def reset(self):
        self.visited = set()
        self.boundary = set()
        self.updates = set()
    def setGrid(self, grid):
        self.height = len(grid)
        if self.height > 0:
            self.width = len(grid[0])
        self.grid = grid

    def seed(self, point):
        self.boundary.add(point)
        self.updates.add(point)

    def update(self):
        temp = set()
        for p in self.boundary:
            x,y = p
            self.grid[y][x] = 0
            if y > 0:
                if self.grid[y-1][x] == 1:
                    temp.add( (x,y-1) )
            if x < self.width - 1:
                if self.grid[y][x+1] == 1:
                    temp.add( (x+1,y) )
            if y < self.height - 1:
                if self.grid[y+1][x] == 1:
                    temp.add( (x,y+1) )
            if x > 0:
                if self.grid[y][x-1] == 1:
                    temp.add( (x-1,y) )
        self.visited |= self.boundary
        self.updates |= temp
        self.boundary = temp

    def getUpdates(self):
        u = self.updates
        self.updates = set()
        return u






