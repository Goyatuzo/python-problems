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


class Orbit:
    def __init__(self, parent, child):
        self.orbits = {}
        self.add_orbit(parent, child)

    def add_orbit(self, parent, child):
        # Find the corrent parent / child
        if parent in self.orbits:
            parent = self.orbits[parent]
        else:
            parent = Node(parent)

        if child in self.orbits:
            child = self.orbits[child]
        else:
            child = Node(child)

        parent.add_child(child)

        self.orbits[parent.data] = parent
        self.orbits[child.data] = child

    def set_root(self):
        all_nodes = set(self.orbits.keys())
        all_children = set([children.data for node in self.orbits.values()
                                  for children in node.children])

        root_node = self.orbits[all_nodes.difference(all_children).pop()]

        self.root = root_node


if __name__ == "__main__":
    orbit = Orbit("parent", "child")
    orbit.add_orbit("child", "grandchild")

    orbit.set_root()

    print(orbit.root.data)
