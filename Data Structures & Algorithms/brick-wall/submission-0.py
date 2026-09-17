class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = defaultdict(int)
        edges = 0
        for row in wall:
            total = 0
            for num in row[:-1]:
                total+= num

                d[total] += 1
                edges = max(edges, d[total])
        
        return len(wall) - edges
