"""
Задание 14. Задача "Острова"

Дан двумерный массив 0/1. Найти количество "островов" (компонент связности).
Использовать DFS или BFS.
"""

from collections import deque


def count_islands_dfs(grid):
    """
    Подсчет количества островов с помощью DFS.
    
    Остров - это группа связанных единиц (1), окруженных нулями (0).
    Связь определяется по горизонтали и вертикали (4 направления).
    
    Временная сложность: O(m * n), где m и n - размеры сетки
    Пространственная сложность: O(m * n) в худшем случае (рекурсивный стек)
    
    Args:
        grid: Двумерный массив 0 и 1
        
    Returns:
        Количество островов
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    island_count = 0
    
    def dfs(row, col):
        """Рекурсивный DFS для пометки всех клеток острова."""
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            visited[row][col] or 
            grid[row][col] == 0):
            return
        
        visited[row][col] = True
        
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                island_count += 1
                dfs(i, j)
    
    return island_count


def count_islands_bfs(grid):
    """
    Подсчет количества островов с помощью BFS.
    
    Временная сложность: O(m * n)
    Пространственная сложность: O(min(m, n)) для очереди в худшем случае
    
    Args:
        grid: Двумерный массив 0 и 1
        
    Returns:
        Количество островов
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    island_count = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(start_row, start_col):
        """BFS для пометки всех клеток острова."""
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    not visited[new_row][new_col] and 
                    grid[new_row][new_col] == 1):
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                island_count += 1
                bfs(i, j)
    
    return island_count


def visualize_grid(grid):
    """Визуализация сетки."""
    print("\nСетка:")
    for row in grid:
        print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    print("=== Задача 'Острова' ===")
    
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    
    visualize_grid(grid1)
    print(f"\nDFS: Количество островов = {count_islands_dfs(grid1)}")
    print(f"BFS: Количество островов = {count_islands_bfs(grid1)}")
    
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    
    visualize_grid(grid2)
    print(f"\nDFS: Количество островов = {count_islands_dfs(grid2)}")
    print(f"BFS: Количество островов = {count_islands_bfs(grid2)}")
    
    grid3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    
    visualize_grid(grid3)
    print(f"\nDFS: Количество островов = {count_islands_dfs(grid3)}")
    print(f"BFS: Количество островов = {count_islands_bfs(grid3)}")
    
    grid4 = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]
    
    visualize_grid(grid4)
    print(f"\nDFS: Количество островов = {count_islands_dfs(grid4)}")
    print(f"BFS: Количество островов = {count_islands_bfs(grid4)}")
    
    grid5 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]
    
    visualize_grid(grid5)
    print(f"\nDFS: Количество островов = {count_islands_dfs(grid5)}")
    print(f"BFS: Количество островов = {count_islands_bfs(grid5)}")


