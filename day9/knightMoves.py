# to find the number of knight moves from square 0, 0 to 8, 8

class graph:
    def __init__(self, target):
        self.visited = [[-1 for _ in range(8)] for _ in range(8)]
        self.target = target
        self.start = (0, 0)

    def movePiece(self, x, y):
        move1 = (x+2, y+1)
        move2 = (x+2, y-1)
        move3 = (x-2, y+1)
        move4 = (x-2, y-1)
        move5 = (x+1, y-2)
        move6 = (x-1, y-2)
        move7 = (x+1, y+2)
        move8 = (x+1, y+2)
        return move1, move2, move3, move4, move5, move6, move7, move8
    
    def inBoundary(self, move):
        return (move[0] < 8 and move[0] > -1 and move[1] < 8 and move[1] > -1) 
    
    def findMoves(self):
        queue = [self.start]
        moves = 0
        while queue:
            for index in range(len(queue)):   
                currentI, currentJ = queue.pop(0)
                if self.visited[currentI][currentJ] != -1:
                    continue
                move1, move2, move3, move4, move5, move6, move7, move8 = self.movePiece(currentI, currentJ)
                if (currentI, currentJ) == self.target:
                    return moves, "found"
                self.visited[currentI][currentJ] = 1
                if self.inBoundary(move1): queue.append(move1)
                if self.inBoundary(move2): queue.append(move2)
                if self.inBoundary(move3): queue.append(move3)
                if self.inBoundary(move4): queue.append(move4)
                if self.inBoundary(move5): queue.append(move5)
                if self.inBoundary(move6): queue.append(move6)
                if self.inBoundary(move7): queue.append(move7)
                if self.inBoundary(move8): queue.append(move8)
            moves += 1
        return "not found"
    
graph1 = graph((4, 4))
print(graph1.findMoves())


        


