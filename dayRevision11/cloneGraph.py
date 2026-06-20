#LEETCODE: 133

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        visited = {}
        def clone(node, visited):
            if node in visited: return visited[node]
            newNode = Node(node.val)
            visited[node] = newNode
            for elements in node.neighbors:
                newNode.neighbors.append(clone(elements, visited))
            return newNode

        return clone(node, visited)