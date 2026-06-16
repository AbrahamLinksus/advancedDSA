class createGraph:
    def __init__(self, n) -> None:
        self.graph = [[0 for _ in range(n)] for _ in range(n)]
        self.visited = [[-1 for _ in range(n)] for _ in range(n)]

        
