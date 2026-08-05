class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
    
        visited = {"0,0": True}
        
        for move in path:
            if move == "N":
                y += 1
            elif move == "E":
                x += 1
            elif move == "S":
                y -= 1
            elif move == "W":
                x -= 1
            
            current_pos = f"{x},{y}"
            
            if current_pos in visited:
                return True
            
            visited[current_pos] = True

        return False
