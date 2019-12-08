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

    def count_orbits(self, depth = 1):
        """Basically counts sum of depth of all children nodes from this node."""
        if self.children == None or len(self.children) == 0:
            return 0

        children_counts = [child.count_orbits(depth + 1) + depth for child in self.children]

        return sum(children_counts)


class Orbit:
    def __init__(self, parent="", child=""):
        self.orbits = {}
        self.root: Node = None

        if parent != "" and child != "":
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

        difference = all_nodes.difference(all_children)
        root_node = self.orbits[difference.pop()]

        self.root = root_node

    def get_orbit_count(self):
        self.set_root()

        return self.root.count_orbits()


if __name__ == "__main__":
    with open('input.txt', 'r') as f:

        line = f.readline()
        orbit = Orbit()

        while line:
            parent, child = line.split(")")

            orbit.add_orbit(parent, child)

            line = f.readline()

        print("Process orbits")
        orbit.set_root()
        print("Root set")
        print(orbit.root.data)
