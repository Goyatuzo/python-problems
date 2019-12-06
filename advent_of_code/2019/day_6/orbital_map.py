class Node:
    """Contain the data for a node in the tree."""

    def __init__(self, name):
        self.data = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def find_node(self, name):
        # If the data matches the query, return true.
        if self.data == name:
            return self

        # If we've reached the end, then we couldn't find it.
        if len(self.children) == 0:
            return None

        results = [child.find_node(name) for child in self.children]

        if any([result != None for result in results]):
            return [result for result in results if result != None][0]
        else:
            return None


# class Orbit:
#     def __init__(self, parent, child):
#         self.add_orbit(parent, child)

#     def add_orbit(self, parent, child):
#         if self.root is None:
#             self.roots = [Node(parent, child)]
