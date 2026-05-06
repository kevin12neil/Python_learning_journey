from collections import deque

print(" HEALTH ACCESS SIMULATION")
print("--------------------------------------------")
print("Legend:")
print("1 = Residential area (people live here)")
print("2 = Healthcare center (hospital/clinic)")
print("3 = Blocked sector (buildings or restricted zone)")
print("0 = Empty land (can walk through)\n")

# Input section
n = int(input("Enter the grid size (e.g., 4 for a 4x4 map): "))
print("\nNow enter the city grid row by row.")
print("Example: For 'Residential, Healthcare, Empty, Blocked' → enter 1203")
print("Make sure each row has exactly", n, "digits (only 0, 1, 2, 3 allowed)\n")

grid = [list(map(int, list(input(f"Row {i+1}: ").strip()))) for i in range(n)]

# Directions (up, down, left, right)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dist = [[-1] * n for _ in range(n)]
q = deque()

# Add all healthcare centers (value 2) as starting points for BFS
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))
            dist[i][j] = 0

# Multi-source BFS to find nearest healthcare for every cell
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 3 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# Analyze distances
max_dist = 0
unreachable = False
unreachable_cells = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            if dist[i][j] == -1:
                unreachable = True
                unreachable_cells.append((i + 1, j + 1))
            else:
                max_dist = max(max_dist, dist[i][j])

# Output section
print("\n--------------------------------------------")
print(" RESULT:")
if unreachable:
    print("  Some residential areas cannot reach any healthcare center.")
    print("Unreachable residential positions (row, column):", unreachable_cells)
else:
    print(" All residential areas can reach a healthcare center.")
    print(f" The maximum minimum distance any resident must walk is {max_dist} steps.")
print("--------------------------------------------")
