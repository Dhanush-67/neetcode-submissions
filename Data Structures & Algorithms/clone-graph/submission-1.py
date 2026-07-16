from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Map to store: {original_node: cloned_node}
        cloned_nodes = {}
        
        # Clone the starting node and register it
        cloned_nodes[node] = Node(node.val)
        
        # Queue for BFS traversal (stores original nodes)
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            # Go through all neighbors of the current original node
            for neighbor in curr.neighbors:
                # If the neighbor hasn't been cloned yet
                if neighbor not in cloned_nodes:
                    # 1. Clone the neighbor
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    # 2. Add the original neighbor to the queue to process later
                    queue.append(neighbor)
                
                # Link the clone of the current node to the clone of its neighbor
                cloned_nodes[curr].neighbors.append(cloned_nodes[neighbor])
                
        return cloned_nodes[node]