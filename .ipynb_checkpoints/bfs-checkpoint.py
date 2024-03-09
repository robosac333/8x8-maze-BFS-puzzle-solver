import numpy as np
from queue import PriorityQueue

class Node:
    def __init__(self, tree_level, node_index, data):
        self.node = (tree_level, [node_index, data])


class BFS:
    def bfs(self, start, goal):

        self.predecessors = {tuple(start.flatten()): None}
        node_index = 0
        layer_index = -1
        node = Node(layer_index, node_index, start)
        pq.put(node.node)
        self.neighbour_list = []
        while not pq.empty():
            current_node = pq.get()
            layer_index += 1
            if np.array_equal(current_node[1][1], goal):
                return get_path(self.predecessors, start, goal)
                # return current_node

            for direction in ["up", "right", "down", "left"]:

                row_offset, col_offset = offsets[direction]
                for i in range(len(current_node[1][1])):
                    for j in range(len(current_node[1][1][i])):
                        if current_node[1][1][i][j] == 0 and i + row_offset >= 0 and i + row_offset < 3 and j + col_offset >= 0 and j + col_offset < 3:
                                neighbour = np.copy(current_node[1][1])
                                neighbour[i + row_offset][j + col_offset] , neighbour[i][j] = neighbour[i][j], neighbour[i + row_offset][j + col_offset]

                                node_index += 1
                                node_tuple = Node(layer_index, node_index, neighbour)

                                if tuple(neighbour.flatten()) not in self.predecessors:
                                    pq.put(node_tuple.node)
                                    self.predecessors[tuple(neighbour.flatten())] = tuple(current_node[1][1].flatten())
                                    self.neighbour_list.append(tuple(neighbour.flatten()))
                                    # print(layer_index, node_index, neighbour)




if __name__ == "__main__":

    offsets = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
    }


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


    # start= np.array([1, 4, 3, 7, 0, 6, 5, 8, 2])
    # start= np.array([2, 1, 7, 8, 6, 0, 3, 4, 5])
    start= np.array([8, 2, 3, 6, 5, 0, 7, 4, 1])
    # goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
    # goal = np.array([1, 4, 3, 7, 8, 6, 0, 5, 2])
    # goal = np.array([8, 2, 1, 6, 0, 7, 3, 4, 5])
    goal = np.array([1, 4, 7, 2, 5, 8, 3, 6, 0])
    start = np.reshape(start, (3, 3))
    goal = np.reshape(goal, (3, 3))

    pq = PriorityQueue()


    bf = BFS()
    path = bf.bfs(start, goal)


    # Open a text file in write mode
    with open(r'C:\Users\sachi\Planning\Project1_Files\nodePath.txt', 'w') as f:
        # Iterate over the numpy array
        for line in path:
            # Convert the elements to strings, join them with spaces, and write to the file
            f.write(' '.join(map(str, line)) + '\n')

    neighbour = bf.neighbour_list
    # # # Open a text file in write mode
    with open(r'C:\Users\sachi\Planning\Project1_Files\Nodes.txt', 'w') as f:
        # Iterate over the numpy array
        for line in neighbour:
            # Convert the elements to strings, join them with spaces, and write to the file
            f.write(' '.join(map(str, line)) + '\n')

    # # Define the list of nodes
    # node_data = [
    #     (0, 0, [0, 3, 6, 4, 3, 1, 7, 8, 2]),
    #     (1, 0, [8, 3, 2, 7, 4, 6, 0, 5, 1]),
    #     (2, 1, [7, 6, 0, 5, 4, 2, 8, 3, 1]),
    #     # Add the rest of your nodes here
    # ]
    # Open a text file in write mode
    # with open('NodesInfo.txt', 'w') as f:
    #     # Write the header to the file
    #     f.write('Node_index\tParent_Node_index\tNode\n')

    #     # Iterate over the list of nodes
    #     for node in node_data:
    #         # Convert the elements to strings, join them with tabs, and write to the file
    #         f.write(f'{node[0]}\t{node[1][0]}\t{" ".join(map(str, node[1][1]))}\n')