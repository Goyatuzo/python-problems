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

    def tests_orbit_add_two(self):
        orbit = Orbit("parent", "child")
        orbit.add_orbit("child", "grandchild")
        orbit.add_orbit("child", "grandchild_two")

        self.assertEqual(["grandchild", "grandchild_two"], [
                         child.data for child in orbit.orbits["child"].children])

    def test_orbit_set_root(self):
        orbit = Orbit("parent", "child")
        orbit.add_orbit("child", "grandchild")
        orbit.set_root()

        self.assertEqual("parent", orbit.root.data)

    def test_given(self):
        orbit = Orbit("COM", "B")
        orbit.add_orbit("B", "C")
        orbit.add_orbit("C", "D")
        orbit.add_orbit("D", "E")
        orbit.add_orbit("E", "F")
        orbit.add_orbit("B", "G")
        orbit.add_orbit("G", "H")
        orbit.add_orbit("D", "I")
        orbit.add_orbit("E", "J")
        orbit.add_orbit("J", "K")
        orbit.add_orbit("K", "L")

        orbit.set_root()
        self.assertEqual("COM", orbit.root.data)
        self.assertEqual(42, orbit.root.count_orbits())

    def test_given_part_two(self):
        orbit = Orbit("COM", "B")
        orbit.add_orbit("B", "C")
        orbit.add_orbit("C", "D")
        orbit.add_orbit("D", "E")
        orbit.add_orbit("E", "F")
        orbit.add_orbit("B", "G")
        orbit.add_orbit("G", "H")
        orbit.add_orbit("D", "I")
        orbit.add_orbit("E", "J")
        orbit.add_orbit("J", "K")
        orbit.add_orbit("K", "L")
        orbit.add_orbit("K", "YOU")
        orbit.add_orbit("I", "SAN")

        orbit.set_root()
        self.assertEqual("COM", orbit.root.data)
        self.assertEqual(4, orbit.root.find_distance("YOU", "SAN"))


if __name__ == '__main__':
    unittest.main()
