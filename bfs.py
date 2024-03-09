# Imported all the required libraries
import numpy as np
from queue import PriorityQueue

# Stored each node as a object of class Node
class Node:
    def __init__(self, tree_level, node_index, parent_index, data):
        self.node = (tree_level, [node_index, parent_index, data])

# Created a class BFS to implement the Breadth First Search algorithm
class BFS:
    def bfs(self, start, goal):

        # Used a predecessor dictionary to store the parent of each node
        self.predecessors = {tuple(start.flatten()): None}

        # Node index, layer index and parent index. Here, layer index is the priority of the node in the Priority Queue
        node_index = 0
        layer_index = -1
        parent_index = 0

        # Initialised a Priority Queue and added lists neighbour_list and neighbour_info_list to store the neighbours and their information
        node = Node(layer_index, node_index, parent_index, start)
        pq.put(node.node)
        self.neighbour_list = []
        self.neighbour_info_list = []

        # Extracted the neighbours of the current node and added them to the Priority Queue if not already present in predecessor as a key
        while not pq.empty():
            current_node = pq.get()
            layer_index += 1
            if np.array_equal(current_node[1][2], goal):
                return get_path(self.predecessors, start, goal)
                # return current_node

            for direction in ["up", "right", "down", "left"]:

                row_offset, col_offset = offsets[direction]
                for i in range(len(current_node[1][2])):
                    for j in range(len(current_node[1][2][i])):
                        if current_node[1][2][i][j] == 0 and i + row_offset >= 0 and i + row_offset < 3 and j + col_offset >= 0 and j + col_offset < 3:
                                neighbour = np.copy(current_node[1][2])
                                neighbour[i + row_offset][j + col_offset] , neighbour[i][j] = neighbour[i][j], neighbour[i + row_offset][j + col_offset]

                                node_index += 1
                                node_tuple = Node(layer_index, node_index, parent_index, neighbour)

                                if tuple(neighbour.flatten()) not in self.predecessors:
                                    pq.put(node_tuple.node)
                                    self.predecessors[tuple(neighbour.flatten())] = tuple(current_node[1][2].flatten())
                                    self.neighbour_list.append(tuple(neighbour.flatten()))
                                    parent_index = current_node[1][0]
                                    self.neighbour_info_list.append((node_index, parent_index, neighbour.flatten()))
                                    # print(layer_index, node_index, parent_index, neighbour)




if __name__ == "__main__":

# Created a dictionary to store the offsets for each direction
    offsets = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
    }

# Function to get the path from the start to the goal
    def get_path(predecessors, start, goal):
        current = tuple(goal.flatten())
        path = []
        while current != tuple(start.flatten()):
            path.append(current)
            current = predecessors[current]
        path.append(tuple(start.flatten()))
        path.reverse()
        # print([char for char in path])
        return path

# Input the start and goal states in columnwise order
    start= np.array([8, 2, 3, 6, 5, 0, 7, 4, 1])
    # start= np.array([2, 1, 7, 8, 6, 0, 3, 4, 5])
    # start= np.array([6, 8, 3, 4, 5, 2, 7, 0, 1])
    goal = np.array([1, 4, 7, 2, 5, 8, 3, 6, 0])



    start = np.reshape(start, (3, 3))
    goal = np.reshape(goal, (3, 3))
    # print(goal)
    pq = PriorityQueue()


    bf = BFS()
    path = bf.bfs(start, goal)


    # Opened a text file in write mode to store the path
    with open(r'C:\Users\sachi\Planning\Project1_Files\nodePath.txt', 'w') as f:
        # Iterateed over the numpy array
        for line in path:
            # Converted the elements to strings, join them with spaces, and write to the file
                f.write(' '.join(map(str, line)) + '\n')


    neighbour = bf.neighbour_list
    with open(r'C:\Users\sachi\Planning\Project1_Files\Nodes.txt', 'w') as f:
        # Iterated over the numpy array
        for line in neighbour:
            # Converted the elements to strings, join them with spaces, and write to the file
            f.write(' '.join(map(str, line)) + '\n')

    # Opened a text file in write mode to store the neighbour information
    with open(r'C:\Users\sachi\Planning\Project1_Files\NodesInfo.txt', 'w') as f:
        f.write('Node_index\tParent_Node_index\tNode\n')
        # Iterated over the list of nodes
        for node in bf.neighbour_info_list:
            # Convertd the elements to strings, join them with tabs, and write to the file
            f.write(f'{node[0]}\t{node[1]}\t{" ".join(map(str, node[2]))}\n')