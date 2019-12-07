import unittest
from unittest.mock import patch

from orbital_map import Node, Orbit


class TestOrbitalMap(unittest.TestCase):
    def test_node(self):
        node = Node("XDF")

        self.assertEqual("XDF", node.data)

    def test_node_add(self):
        node = Node("XDF")
        node.add_child(Node("ASD"))
        node.add_child(Node("QWE"))

        self.assertEqual(["ASD", "QWE"], [n.data for n in node.children])

    def test_node_find(self):
        node = Node("XDF")
        node.add_child(Node("QWE"))
        node.children[0].add_child(Node("ASD"))

        found = node.find_node("ASD")

        self.assertEqual("ASD", found.data)

    def test_orbit_add(self):
        orbit = Orbit("parent", "child")
        orbit.add_orbit("child", "grandchild")

        self.assertEqual(["parent", "child", "grandchild"], [
                         value.data for value in orbit.orbits.values()])

    def test_orbit_set_root(self):
        orbit = Orbit("parent", "child")
        orbit.add_orbit("child", "grandchild")
        orbit.set_root()

        self.assertEqual("parent", orbit.root.data)

if __name__ == '__main__':
    unittest.main()
