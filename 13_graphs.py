"""
Задание 13. Графы

Реализация хранения графов (матрица смежности и список смежности)
и алгоритмов BFS, DFS, поиск кратчайшего пути.
"""

from collections import deque, defaultdict


class GraphAdjacencyMatrix:
    """
    Граф на основе матрицы смежности.
    """
    
    def __init__(self, num_vertices: int, directed: bool = False):
        """
        Инициализация графа.
        
        Args:
            num_vertices: Количество вершин
            directed: Направленный граф или нет
        """
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, from_vertex: int, to_vertex: int, weight: int = 1):
        """
        Добавление ребра.
        
        Временная сложность: O(1)
        """
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            self.matrix[from_vertex][to_vertex] = weight
            if not self.directed:
                self.matrix[to_vertex][from_vertex] = weight
    
    def get_neighbors(self, vertex: int) -> list:
        """
        Получение соседей вершины.
        
        Временная сложность: O(V), где V - количество вершин
        """
        neighbors = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] != 0:
                neighbors.append(i)
        return neighbors
    
    def bfs(self, start: int) -> list:
        """
        Обход графа в ширину (BFS).
        
        Временная сложность: O(V + E), где V - вершины, E - ребра
        Пространственная сложность: O(V)
        
        Args:
            start: Начальная вершина
            
        Returns:
            Список вершин в порядке обхода BFS
        """
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start: int) -> list:
        """
        Обход графа в глубину (DFS).
        
        Временная сложность: O(V + E)
        Пространственная сложность: O(V)
        
        Args:
            start: Начальная вершина
            
        Returns:
            Список вершин в порядке обхода DFS
        """
        visited = [False] * self.num_vertices
        result = []
        
        def dfs_recursive(vertex: int):
            visited[vertex] = True
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if not visited[neighbor]:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def shortest_path_bfs(self, start: int, end: int) -> list:
        """
        Поиск кратчайшего пути в невзвешенном графе с помощью BFS.
        
        Временная сложность: O(V + E)
        
        Args:
            start: Начальная вершина
            end: Конечная вершина
            
        Returns:
            Список вершин, образующих кратчайший путь, или пустой список если путь не найден
        """
        if start == end:
            return [start]
        
        visited = [False] * self.num_vertices
        parent = [-1] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        
        while queue:
            vertex = queue.popleft()
            
            if vertex == end:
                path = []
                current = end
                while current != -1:
                    path.append(current)
                    current = parent[current]
                return path[::-1]
            
            for neighbor in self.get_neighbors(vertex):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = vertex
                    queue.append(neighbor)
        
        return []


class GraphAdjacencyList:
    """
    Граф на основе списка смежности.
    """
    
    def __init__(self, directed: bool = False):
        """
        Инициализация графа.
        
        Args:
            directed: Направленный граф или нет
        """
        self.directed = directed
        self.adj_list = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, from_vertex, to_vertex, weight: int = 1):
        """
        Добавление ребра.
        
        Временная сложность: O(1)
        """
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)
        self.adj_list[from_vertex].append((to_vertex, weight))
        
        if not self.directed:
            self.adj_list[to_vertex].append((from_vertex, weight))
    
    def get_neighbors(self, vertex):
        """
        Получение соседей вершины.
        
        Временная сложность: O(1) в среднем случае
        """
        return [neighbor for neighbor, _ in self.adj_list.get(vertex, [])]
    
    def bfs(self, start):
        """
        Обход графа в ширину (BFS).
        
        Временная сложность: O(V + E)
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Обход графа в глубину (DFS).
        
        Временная сложность: O(V + E)
        """
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def shortest_path_bfs(self, start, end) -> list:
        """
        Поиск кратчайшего пути в невзвешенном графе с помощью BFS.
        
        Временная сложность: O(V + E)
        """
        if start == end:
            return [start]
        
        visited = set()
        parent = {}
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            
            if vertex == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent.get(current)
                return path[::-1]
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = vertex
                    queue.append(neighbor)
        
        return []


if __name__ == "__main__":
    print("=== Тестирование графа на матрице смежности ===")
    
    graph_matrix = GraphAdjacencyMatrix(6, directed=False)
    graph_matrix.add_edge(0, 1)
    graph_matrix.add_edge(0, 2)
    graph_matrix.add_edge(1, 3)
    graph_matrix.add_edge(2, 4)
    graph_matrix.add_edge(3, 5)
    graph_matrix.add_edge(4, 5)
    
    print("Граф:")
    print("  0 -- 1 -- 3")
    print("  |         |")
    print("  2 -- 4 -- 5")
    
    print(f"\nBFS начиная с 0: {graph_matrix.bfs(0)}")
    print(f"DFS начиная с 0: {graph_matrix.dfs(0)}")
    print(f"Кратчайший путь от 0 до 5: {graph_matrix.shortest_path_bfs(0, 5)}")
    
    print("\n=== Тестирование графа на списке смежности ===")
    
    graph_list = GraphAdjacencyList(directed=False)
    graph_list.add_edge(0, 1)
    graph_list.add_edge(0, 2)
    graph_list.add_edge(1, 3)
    graph_list.add_edge(2, 4)
    graph_list.add_edge(3, 5)
    graph_list.add_edge(4, 5)
    
    print(f"BFS начиная с 0: {graph_list.bfs(0)}")
    print(f"DFS начиная с 0: {graph_list.dfs(0)}")
    print(f"Кратчайший путь от 0 до 5: {graph_list.shortest_path_bfs(0, 5)}")
    
    print("\n=== Тест с более сложным графом ===")
    complex_graph = GraphAdjacencyList(directed=False)
    complex_graph.add_edge('A', 'B')
    complex_graph.add_edge('A', 'C')
    complex_graph.add_edge('B', 'D')
    complex_graph.add_edge('B', 'E')
    complex_graph.add_edge('C', 'F')
    complex_graph.add_edge('D', 'G')
    complex_graph.add_edge('E', 'G')
    complex_graph.add_edge('F', 'G')
    
    print(f"BFS начиная с 'A': {complex_graph.bfs('A')}")
    print(f"DFS начиная с 'A': {complex_graph.dfs('A')}")
    print(f"Кратчайший путь от 'A' до 'G': {complex_graph.shortest_path_bfs('A', 'G')}")


